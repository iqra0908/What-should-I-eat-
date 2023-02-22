from flask import jsonify
from Recipes import Recipes
from flask import Response
from flask import Flask, request, render_template

app = Flask(__name__)
recipes = Recipes('data/RAW_recipes.csv')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/recipes', methods=['GET'])
def getRecipes():
    return recipes.getRecipes()

@app.route('/recipesByIngredients', methods=['POST'])
def getRecipesByIngredients():
    my_ing = request.form['ingredients']
    my_ing = my_ing.split(",")
    return Response(recipes.getRecipesByIngredients(my_ing), content_type='application/json')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
