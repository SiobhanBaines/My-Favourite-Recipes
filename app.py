import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route('/like/<recipe_id>', methods=["GET", "POST"])
def like(recipe_id):
    recipe = mongo.db.recipe.update_one(
        {"_id": ObjectId(recipe_id)},
        {'$inc': {'likes': 1}},
        upsert=True
        )
    recipes = list(mongo.db.recipe.find())
    return render_template("recipe.html", recipes=recipes)


@app.route('/dislike/<recipe_id>', methods=["GET", "POST"])
def dislike(recipe_id):
    recipe = mongo.db.recipe.update_one(
        {"_id": ObjectId(recipe_id)},
        {'$inc': {'dislikes': 1}},
        upsert=True
    )
    recipes = list(mongo.db.recipe.find())
    return render_template("recipe.html", recipes=recipes)


@app.route("/get_weight_measure")
def get_weight_measure():
    measures = mongo.db.measures.find()
    temperatures = mongo.db.temperatures.find()
    return render_template(
        "weight_measure.html", measures=measures, temperatures=temperatures)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
