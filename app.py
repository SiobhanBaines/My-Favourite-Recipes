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


@app.route('/recipe_detail/<recipe_id>')
def recipe_detail(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}, {"ingredients"})
    method = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}, {"method"})
    return render_template(
        "recipe_detail.html", recipe=recipe, method_list=method, ingredient_list=ingredients)


@app.route('/like/<recipe_id>', methods=["GET", "POST"])
def like(recipe_id):
    print(recipe_id)
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
    print(username)
    print(user_id)
    print(session["user"])
    if session["user"]:
        recipes = mongo.db.recipes.find({"user": ObjectId(user_id)})
        print(recipes)

        return render_template(
            "profile.html", username=username.capitalize(), recipes=recipes)

    return redirect(url_for("login"))


@app.route("/maintain_recipe/<recipe_id>", methods=["GET", "POST"])
def maintain_recipe(recipe_id):   
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}, {"ingredients"})
    method = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}, {"method"})
    return render_template(
        "maintain_recipe.html", recipe=recipe, method_list=method, ingredient_list=ingredients)



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
