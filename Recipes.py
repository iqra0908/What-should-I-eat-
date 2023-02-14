import pandas as pd


class Recipes:
  def __init__(self, filename):
    self.df = pd.read_csv (filename)
    
  def getRecipes(self):
    return self.df.head(10).to_json(orient='records')

# print 1 recipie below 
#print (Recipes('data/RAW_recipes.csv').getRecipes())
