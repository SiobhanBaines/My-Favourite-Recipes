import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

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


@app.route('/recipe_detail/<recipe_id>')
def recipe_detail(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)}, {"ingredients"})
    method = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)}, {"method"})
    return render_template(
        "recipe_detail.html", recipe=recipe,
        method_list=method, ingredient_list=ingredients)


@app.route('/like/<recipe_id>', methods=["GET", "POST"])
def like(recipe_id):
    recipe = mongo.db.recipes.update_one(
        {"_id": ObjectId(recipe_id)},
        {'$inc': {'likes': 1}},
        upsert=True
        )
    recipes = list(mongo.db.recipe.find())
    return render_template("recipe.html", recipes=recipes)


@app.route('/dislike/<recipe_id>', methods=["GET", "POST"])
def dislike(recipe_id):
    recipe = mongo.db.recipes.update_one(
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

        if user_exists:
            flash("Username Already Exists")
            return redirect(url_for("register"))

        # check passwords match
        if {request.form.get(
                "password").lower()} != {request.form.get(
                "confirm-password").lower()}:
            flash("Passwords Do Not Match")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "image": ""
        }
        mongo.db.users.insert_one(register)

        # put new user into 'session cookie
        session["user"] = request.form.get("username").lower()
        flash("Successful Registration. You can now add your own recipes")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    image = mongo.db.users.find_one(
        {"username": session["user"]})["image"]
    if session["user"]:
        recipes = mongo.db.recipes.find({"user": ObjectId(user_id)})

        return render_template(
            "profile.html", username=username.capitalize(),
            image=image, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/change_password/<username>", methods=['GET', 'POST'])
def change_password(username):
    return render_template("profile", username=username)


@app.route("/delete_account/<username>", methods=['GET', 'POST'])
def delete_account(username):
    # prevents guest users from viewing the form
    print(username)
    if 'username' not in session:
        flash('You must be logged in to delete an account!')
    user = mongo.db.users.find_one({"username": username})
    # checks if password matches existing password in database
    if check_password_hash(user["password"],
                           request.form.get("confirm_password_to_delete")):

        user_recipes = user.get("recipes")
        for recipe in user_recipes:
            mongo.db.recipes.remove({"_id": recipe})

        # remove user from database,clear session and redirect to the home page
        flash("Your account has been deleted.")
        session.pop("username", None)
        mongo.db.users.remove({"_id": user.get("_id")})
        return redirect(url_for("homepage"))
    else:
        flash("Password is incorrect! Please try again")
        return redirect(url_for("profile", username=username))


@app.route("/maintain_recipe/<recipe_id>", methods=["GET", "POST"])
def maintain_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)}, {"ingredients"})
    method = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)}, {"method"})
    return render_template(
        "maintain_recipe.html", recipe=recipe,
        method_list=method, ingredient_list=ingredients)


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category": request.form.get("category"),
            "user": session["user"],
            "date": datetime.now()
            }
 
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    categories = list(mongo.db.categories.find().sort("category", 1))

    return render_template("add_recipe.html")


@app.route("/logout")
def logout():
    # log user out by removing user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
