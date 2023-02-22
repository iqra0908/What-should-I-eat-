import pandas as pd
import ast
import json


class Recipes:
  def __init__(self, filename):
    self.df = pd.read_csv (filename)
    
  def getRecipes(self):
    return list(self.df.head(10).to_dict(orient='records'))

  
  def match_ingredient(self, ingredients, my_ing):
    if not isinstance(ingredients, list):
        return False
    ingredients = [ing.lower() for ing in ingredients]  # convert the ingredients to lowercase
    num_matches = sum(1 for ing in ingredients if any(item in ing for item in my_ing))
    return num_matches >= 0.9 * len(my_ing)
  
  def getRecipesByIngredients(self, my_ing):
    my_ing_lower = [ing.lower() for ing in my_ing]
    my_ing_set = set(my_ing_lower)
    df = self.df.copy()
    # convert the string representation of the list of ingredients into an actual list of ingredients
    df['ingredients'] = df['ingredients'].apply(ast.literal_eval)

    # filter the dataframe based on whether it contains at least 80% of the ingredients in my_ing
    filtered_df = df[df['ingredients'].apply(self.match_ingredient,args=(my_ing_set,))]

    filtered_df.reset_index(drop=True,inplace=True)
    return filtered_df.to_json(orient='index')
  
# create main for this class
if __name__ == "__main__":
  recipes = Recipes('data/RAW_recipes.csv')
  my_ing = ['salt', 'pepper', 'onion', 'bell pepper', 'potatoes','shallots','parsley','tarragon','olive oil', 
          'cheese','vinegar']
  print(recipes.getRecipesByIngredients(my_ing))