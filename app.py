import os
import json
from Recipes import Recipes
from flask import Flask, request, render_template

app = Flask(__name__)
recipes = Recipes('data/RAW_recipes.csv')

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/recipes')
def getRecipes():
    return json.loads(recipes.getRecipes())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
