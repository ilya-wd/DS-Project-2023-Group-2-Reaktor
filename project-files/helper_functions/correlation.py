from scipy.special import comb
import pandas as pd
import numpy as np
import scipy.misc
scipy.misc.comb = comb
import h3

class correaltion():
    def __init__(self):
        pass

    def relative_location_info(self, species1: str, species2: str, dataframe: pd.DataFrame) -> dict:
        """ 
        Returns relative location information of two species in the 
        specified data frame. Pass in the names of the columns in the dataframe
        that contain species1 and species2 counts per location.
        Note that the overall mean counts are averages over the areas in which the species
        exists (so, a species that has 2 observations in 1 location will get a mean of 2).
        """
        # filters in only rows where species 1 exists
        species1_df = dataframe.loc[dataframe[species1] >= 1]
        # filters in rows where also species 2 exists 
        # (interesection)
        species1_and_species2 = species1_df.loc[species1_df[species2] >= 1]
        # filters out rows where species 2 exists
        species1_not_species2 = species1_df.loc[species1_df[species2] >= 0]
        
        # filters in only rows where species 2 exists
        species2_df = dataframe.loc[dataframe[species2] >= 1]
        # filters in rows where also species 1 exists 
        # (interesection from the other direction: should be the same as species1_and_species2)
        species2_and_species1 = species2_df.loc[species2_df[species1] >= 1]
        # filters out rows where species 1 exists
        species2_not_species1 = species2_df.loc[species2_df[species1] >= 0]
    
        if not species1_and_species2.shape[0] == species2_and_species1.shape[0]:
            raise Exception('Dataframe compromised: the intersection calculations resulted in differing values.')  
        
        return {"intersection_count": species1_and_species2.shape[0], 
                "species1_count": species1_df.shape[0], 
                "species2_count": species2_df.shape[0],
                "species1_overall_mean": species1_df[species1].mean(),
                "species2_overall_mean": species2_df[species2].mean(),
                "species1_where2_mean": species1_and_species2[species1].mean(),
                "species2_where1_mean": species2_and_species1[species2].mean(),
                "species1_not2_mean": species1_not_species2[species1].mean(),
                "species1_not2_mean": species2_not_species1[species2].mean()}