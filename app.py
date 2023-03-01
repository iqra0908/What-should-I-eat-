from Recipes import Recipes
from flask import Flask, request, render_template

app = Flask(__name__)
recipes = Recipes('data/recipes.pkl.gz')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/recipes', methods=['GET'])
def getRecipes():
    return recipes.getRecipes()

@app.route('/recipesByIngredients', methods=['GET'])
def getRecipesByIngredients():
    my_ing = request.args.get('ingredients')
    my_ing = my_ing.split(",")
    return recipes.getRecipesByIngredients(my_ing)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
