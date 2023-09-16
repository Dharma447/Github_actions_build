import pandas as pd


class pandas_operations:

  def __init__(self, df1, df2):
    self.df1 = df1
    self.df2 = df2

  def return_concate(self):
    return pd.concat(self.df1, self.df2)
    
