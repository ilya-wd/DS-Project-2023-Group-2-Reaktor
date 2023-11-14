import numpy as np
import pandas as pd
from scipy.stats import beta, dirichlet

class InferenceModel:
    def __init__ (self, area_column : str, species_column : str) -> None:
        """
        Initialization with:
            - area_column : name of column in pandas DataFrame that contains area identification
            - species_column : name of column in pandas DataFrame that contains species identification
        """
        self.area_column = area_column
        self.species_column = species_column

    def fit(self, input_df : pd.DataFrame) -> pd.DataFrame:
        """
        Function to map actual data to inferred distribution
        :param pd.DataFrame input_df: Dataframe of recorded observations
        :return pd.DataFrame: Dataframe of inferred distribution
        Note: input_df should contain columns as specified in model initialization (area_column and species_column)
        """

        # updates self.obs_data with preprocessed
        self.obs_data = self.__preprocess (input_df)
        return self.obs_data

    def __preprocess (self, dataframe : pd.DataFrame) -> pd.DataFrame:
        """
        Private function to group and pivot dataframe
        :param pd.DataFrame dataframe: Dataframe to preprocess, containing columns specified in model intialization
        :return pd.DataFrame: Dataframe with area identifiers as indices, species indentiers as columns, and counts of obervations as values
        """

        # groups input dataframe by area and species identifiers
        grouped_df = dataframe.groupby([self.area_column, self.species_column]).count()
        grouped_df.reset_index(inplace = True)

        # modifies columns of grouped data frame to [area_column, species_column, nof_obs]
        columns_to_drop = list(filter(lambda name : name not in [self.area_column, self.species_column], grouped_df.columns))
        grouped_df = grouped_df.drop(columns = columns_to_drop[1:])
        grouped_df.columns = [self.area_column, self.species_column] + ["nof_obs"]

        # pivots grouped dataframe with area_column = index, species_column = column, nof_obs = values
        pivoted_df = grouped_df.pivot(index = self.area_column, columns = self.species_column, values = "nof_obs")
        pivoted_df = pivoted_df.fillna(0.0)

        # returns pivoted dataframe
        return pivoted_df

class ActualDistribution (InferenceModel):
    def fit(self, input_df):
        super().fit(input_df)
        def calculate_percentage (area_row):
            row_np = area_row.to_numpy()
            return row_np / np.sum(area_row)
        self.dist_data = pd.DataFrame(list(self.obs_data.apply(lambda row : calculate_percentage(row), axis = 1)))
        self.dist_data.columns = self.obs_data.columns
        self.dist_data[self.area_column] = self.obs_data.index
        self.dist_data.set_index(self.area_column, inplace = True)
        return self.dist_data

class InferDistribution (InferenceModel):
    def __init__ (self, area_column, species_column, neighbor_finder, neighbor_penalty):
        super().__init__(area_column, species_column)
        self.neighbor_finder = neighbor_finder
        self.neighbor_penalty = neighbor_penalty

    def fit(self, input_df):
        super().fit(input_df)
        self.neighbors_data = self.__aggregate()

    def __aggregate (self):
        def aggregate_neighboring_rows (area_id):
            neighbors = self.neighbor_finder(area_id)
            neighbors_obs = self.obs_data[self.obs_data.index.isin(neighbors)]
            neighbors_sum = neighbors_obs.sum().to_dict()
            return neighbors_sum
        
        neighbors_data = pd.DataFrame(list(self.obs_data.apply(
            lambda row: aggregate_neighboring_rows(row.name), axis = 1
        )))
        neighbors_data[self.area_column] = self.obs_data.index
        neighbors_data.set_index(self.area_column, inplace = True)
        return neighbors_data

class BetaDistribution (InferDistribution):
    def __init__ (self, area_column, species_column, neighbor_finder, neighbor_penalty, species):
        super().__init__(area_column, species_column, neighbor_finder, neighbor_penalty)
        self.species = species

    def __initiate_prior (self, row):
        successes = row[self.species]
        trials = row[:-1].sum()
        alpha = 1. + successes*self.neighbor_penalty
        beta = 1. + (trials - successes)*self.neighbor_penalty
        return alpha, beta
    
    def __update_posterior (self, prior_alpha, prior_beta, row):
        successes = row[self.species]
        trials = row[:-1].sum()
        alpha = prior_alpha + successes
        beta = prior_beta + (trials - successes)
        return alpha, beta
    
    def __calculate_params (self, area_id):
        prior_alpha, prior_beta = self.__initiate_prior(self.neighbors_data.loc[area_id])
        alpha, beta = self.__update_posterior(prior_alpha, prior_beta, self.obs_data.loc[area_id])
        return {
            self.area_column : area_id,
            "prior_alpha" : prior_alpha,
            "prior_beta" : prior_beta,
            "alpha" : alpha,
            "beta" :  beta
        }
    
    def fit(self, input_df):
        super().fit(input_df)
        
        self.dist_data = pd.DataFrame(list(self.obs_data.apply(lambda row : self.__calculate_params(row.name), axis = 1)))
        self.dist_data[["mean", "variance", "skew"]] = self.dist_data.apply(lambda row : beta.stats(row["alpha"], row["beta"], moments = "mvs"), axis=1, result_type='expand')
        self.dist_data["median"] = self.dist_data.apply(lambda row : beta.median(row["alpha"], row["beta"]), axis=1)
        self.dist_data["50%"] = self.dist_data.apply(lambda row : beta.interval(0.5, row["alpha"], row["beta"]), axis=1)
        self.dist_data["90%"] = self.dist_data.apply(lambda row : beta.interval(0.9, row["alpha"], row["beta"]), axis=1)
        self.dist_data["95%"] = self.dist_data.apply(lambda row : beta.interval(0.95, row["alpha"], row["beta"]), axis=1)
        self.dist_data.set_index(self.area_column, inplace = True)
        return self.dist_data

class DirichletDistribution (InferDistribution):
    def __initiate_prior (self, row):
        pass
    
    def __update_posterior (self, prior_alpha, row):
        successes = row.to_numpy()
        return prior_alpha + successes
    
    def __calculate_params (self, area_id, initiate_prior_func, update_posterior_func):
        prior_alpha = initiate_prior_func (self.neighbors_data.loc[area_id])
        alpha = update_posterior_func (prior_alpha, self.obs_data)
        return alpha
    
    def fit(self, input_df, initiate_prior_func = None, update_posterior_func = None):
        super().fit(input_df)
        if initiate_prior_func == None:
            initiate_prior_func = self.__initiate_prior
        if update_posterior_func == None:
            update_posterior_func = self.__update_posterior
        self.alphas = pd.DataFrame(columns = self.obs_data.columns)
        alphas = self.obs_data.apply(lambda row: self.__calculate_params(row.name, initiate_prior_func, update_posterior_func), axis = 1)
        alphas = alphas.tolist()
        alphas = alphas[0]
        for row in alphas:
            self.alphas.loc[len(self.alphas.index)] = list(row)
        self.alphas[self.area_column] = self.obs_data.index
        self.alphas.set_index(self.area_column, inplace = True)

        self.dist_data = pd.DataFrame(columns = self.obs_data.columns)
        for row in self.alphas.apply(lambda row : dirichlet.mean(row.to_numpy()), axis = 1):
            self.dist_data.loc[len(self.dist_data.index)] = list(row)
        self.dist_data[self.area_column] = self.obs_data.index
        self.dist_data.set_index(self.area_column, inplace = True)

        self.variances = pd.DataFrame(columns = self.obs_data.columns)
        for row in self.alphas.apply(lambda row : dirichlet.var(row.to_numpy()), axis = 1):
            self.variances.loc[len(self.variances.index)] = list(row)
        self.variances[self.area_column] = self.obs_data.index
        self.variances.set_index(self.area_column, inplace = True)
        return self.dist_data
    
class UniformDirichletDistribution (DirichletDistribution):
    def __initiate_prior (self, row):
        successes = row.to_numpy()
        return 1. + successes * self.neighbor_penalty
    
    def fit(self, input_df):
        return super().fit(input_df, initiate_prior_func=self.__initiate_prior)

class SelectiveDirichletDistribution (DirichletDistribution):
    def __initiate_prior (self, row):
        successes = row.to_numpy()
        unobserved_count = np.count_nonzero(successes == 0.0)
        prior = np.where(successes == 0.0, 1. / unobserved_count, 1)
        return prior + successes*self.neighbor_penalty
    
    def fit(self, input_df):
        return super().fit(input_df, initiate_prior_func=self.__initiate_prior)
    
class SpeciesPruner():
    def __init__(self, nof_species, threshold_obs = 100) -> None:
        assert nof_species > 1
        prior = np.full(nof_species, 1)
        prior[nof_species - 1] = 1 + threshold_obs
        posterior = dirichlet.mean(prior)
        self.probability_threshold = posterior[0]

    def __prune_percentage (self, row):
        np_row = row.to_numpy()
        unnormalized = np.where(np_row < self.probability_threshold, 0.0, np_row)
        return unnormalized / np.sum(unnormalized)
    
    def fit (self, dist_data: pd.DataFrame) -> pd.DataFrame:
        pruned_df = pd.DataFrame(columns = dist_data.columns)
        for row in dist_data.apply(self.__prune_percentage, axis = 1):
            pruned_df.loc[len(pruned_df.index)] = list(row)
        pruned_df[dist_data.index.name] = dist_data.index
        pruned_df.set_index(dist_data.index.name, inplace = True)
        return pruned_df