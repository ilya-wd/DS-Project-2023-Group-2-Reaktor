import h3
import pandas as pd

class h3_grid():
  def __init__(self, resolution=5):
    self.resolution = resolution
    self.grid = False

  def row_to_h3cell(self, row) -> str:
    """
    Function to return the h3 grid index of the input row.
    :param pd.Series row: The row to be loaded.
    """
    return h3.geo_to_h3(lat=row['Latitude'], lng=row['Longitude'], resolution = self.resolution)
    
  def fit(self, df: pd.DataFrame):
    """
    Function to load data into a hexagonal grid.
    :param pd.DataFrame df: The data frame to be loaded.
    """
    df['h3_cell'] = df.apply(self.row_to_h3cell, axis=1)
    df = df.reset_index(drop=False).groupby('h3_cell').index.agg(list).to_frame("observations_id").reset_index()
    df['count'] = df['observations_id'].apply(lambda row: len(row))
    df['neighbors'] = df['h3_cell'].apply(lambda h3_index: h3.k_ring(h3_index, 1))
    self.grid = df

  def grid_info(self) -> pd.DataFrame:
    """
    Function to return the h3 grid groupings as a data frame.
    :param pd.DataFrame df: The data frame to be loaded.
    :return pd.DataFrame: A data frame with columns for cell index, list of cells in the grid, a count of observations in the cell, and the indices of the neigbours of the cell.
    """
    if not isinstance(self.grid, pd.DataFrame):
      raise Exception('Data not loaded. Use fit() first.')  
    
    return self.grid 