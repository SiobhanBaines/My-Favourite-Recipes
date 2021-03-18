import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
    recipes = mongo.db.recipes.find()
    return render_template("home.html", recipes=recipes)


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


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check user already exists
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        print(user_exists)

        if user_exists:
            flash("Username Already Exists")
            print("Username Already Exists")
            return redirect(url_for("register"))

        # check passwords match
        if {request.form.get(
                "password").lower()} != {request.form.get(
                "confirm-password").lower()}:
            flash("Passwords Do Not Match")
            print("Passwords Do Not Match")
            return redirect(url_for("register"))
        print("Valid user and password")
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into 'session cookie
        session["user"] = request.form.get("username").lower()
        flash("Successful Registration. You can now add your own recipes")

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check user already exists
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            # check passwords match
            if check_password_hash(
                    user_exists["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        
        else:
            # invalid username
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
