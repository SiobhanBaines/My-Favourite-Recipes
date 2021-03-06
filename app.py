import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import cloudinary
import cloudinary.uploader
import cloudinary.api
from datetime import datetime

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Cloudinary copied from Double Shamrock Hackathon
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    recipes = mongo.db.recipes.find()
    return render_template("home.html", recipes=recipes)


@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template(
        "recipes.html", recipes=recipes)


@app.route('/search', methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template(
        "recipes.html", recipes=recipes)


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
    if request.method == "POST":
        liked = mongo.db.likedRecipes.find_one(
            {"recipe_id": ObjectId(recipe_id), "username": session["user"]})
        if liked:
            flash("Sorry, you have already liked this recipe.")
            return redirect(
                url_for(
                    "recipe_detail", recipe_id=recipe_id,
                    _external=True, _scheme='https'))
        else:
            recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
            recipe = mongo.db.recipes.update_one(
                {"_id": ObjectId(recipe_id)},
                {'$inc': {'likes': 1}},
                upsert=True
            )
            likedRecipe = {
                "recipe_id": ObjectId(recipe_id),
                "username": session["user"]
                }
            mongo.db.likedRecipes.insert_one(likedRecipe)
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)}, {"ingredients"})
    method = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)}, {"method"})
    return render_template(
        "recipe_detail.html", recipe=recipe,
        method_list=method, ingredient_list=ingredients)


@app.route('/dislike/<recipe_id>', methods=["GET", "POST"])
def dislike(recipe_id):
    if session.get('user'):
        if session['user']:
            if request.method == "POST":
                disliked = mongo.db.dislikedRecipes.find_one(
                    {"recipe_id": ObjectId(recipe_id),
                        "username": session["user"]})
                if disliked:
                    flash("Sorry, you have already disliked this recipe.")
                    return redirect(
                        url_for(
                            "recipe_detail",
                            recipe_id=recipe_id,
                            _external=True, _scheme='https'))
                else:
                    recipe = mongo.db.recipes.update_one(
                        {"_id": ObjectId(recipe_id)},
                        {'$inc': {'dislikes': 1}},
                        upsert=True
                    )
                    dislikedRecipe = {
                        "recipe_id": ObjectId(recipe_id),
                        "username": session["user"]
                    }
                    mongo.db.dislikedRecipes.insert_one(dislikedRecipe)
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)}, {"ingredients"})
    method = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)}, {"method"})
    return render_template(
        "recipe_detail.html", recipe=recipe,
        method_list=method, ingredient_list=ingredients)


@app.route("/add_recipe/", methods=["GET", "POST"])
def add_recipe():
    user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
    if request.method == "POST":
        recipe_id = request.form.get("recipe_id")
        submit_recipe = {
            "user": user_id,
            "category": request.form.get("category"),
            "title": request.form.get("title"),
            "image": request.form.get("image_url"),
            "servings": request.form.get("servings"),
            "prep_time": (int)(request.form.get("prep_time")),
            "cook_time": (int)(request.form.get("cook_time")),
            "temperature": request.form.get("temperature"),
            "temp_unit": request.form.get("temp_unit"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "note": request.form.get("notes"),
            "likes": 0,
            "dislikes": 0,
            "name": session["user"],
            "date": datetime.now()
        }
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        if recipe:
            mongo.db.recipes.update(
                {"_id": ObjectId(recipe_id)}, submit_recipe, upsert=True)
        else:
            mongo.db.recipes.insert_one(submit_recipe)
        flash("Recipe Successfully Added")
        return redirect(
            url_for(
                "profile", username=session["user"],
                _external=True, _scheme='https'))
    categories = list(mongo.db.categories.find().sort("category", 1))
    recipe = mongo.db.recipes.find().sort([('timestamp', -1)]).limit(1)
    return render_template(
        "add_recipe.html", recipe=recipe, categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
        submit_recipe = {
            "user": user_id,
            "category": request.form.get("category"),
            "title": request.form.get("title"),
            "image": request.form.get("image_url"),
            "servings": request.form.get("servings"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "temperature": request.form.get("temperature"),
            "temp_unit": request.form.get("temp_unit"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "note": request.form.get("notes"),
            "name": session["user"],
            "date": datetime.now()
        }
        mongo.db.recipes.update(
            {"_id": ObjectId(recipe_id)}, submit_recipe, upsert=True)
        flash("Recipe Successfully Updated")
        return redirect(
            url_for(
                "profile", username=session["user"],
                _external=True, _scheme='https'))
    recipe = (mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}))
    categories = mongo.db.categories.find()
    return render_template(
        "update_recipe.html", recipe_id=recipe_id, recipe=recipe,
        categories=categories)


@app.route("/delete_recipe/<recipe_id>", methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    username = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})["name"]
    if request.method == 'POST':
        # prevents guest users from viewing the form
        if {username == session["user"] or session["user"] == "admin"}:
            user = mongo.db.users.find_one({"username": session["user"]})
            # checks if password matches existing password in database
            if check_password_hash(
                user["password"], request.form.get(
                    "confirm-password-to-delete")):
                # delete recipe created by user
                mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
                flash("Recipe Successfully Deleted")
            else:
                flash("Password is incorrect! Please try again")
                return redirect(
                    url_for(
                        'edit_recipe', recipe_id=recipe_id,
                        _external=True, _scheme='https'))
        else:
            flash("You are not authorised to delete this recipe")
    return redirect(
        url_for(
            'profile', username=session['user'],
            _external=True, _scheme='https'))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check user already exists
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if user_exists:
            flash("Username Already Exists")
            return redirect(
                url_for("register", _external=True, _scheme='https'))
        # check passwords match
        if {request.form.get(
                "password").lower()} != {request.form.get(
                "confirm-password").lower()}:
            flash("Passwords Do Not Match")
            return redirect(
                url_for("register", _external=True, _scheme='https'))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "image": ""
        }
        mongo.db.users.insert_one(register)
        # put new user into 'session cookie
        session["user"] = request.form.get("username").lower()
        flash("Successful Registration. You can now add your own recipes")
        return redirect(
            url_for(
                "profile", username=session["user"],
                _external=True, _scheme='https'))
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
                return redirect(
                    url_for(
                        "profile", username=session["user"],
                        _external=True, _scheme='https'))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(
                    url_for("login", _external=True, _scheme='https'))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(
                url_for("login", _external=True, _scheme='https'))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    image = mongo.db.users.find_one(
        {"username": session["user"]})["image"]
    if session["user"] == "admin":
        recipes = list(mongo.db.recipes.find().sort("recipe", 1))
    else:
        if session["user"]:
            recipes = list(mongo.db.recipes.find(
                {"user": ObjectId(user_id)}).sort("category", 1))
        else:
            return redirect(url_for("login", _external=True, _scheme='https'))
    categories = mongo.db.categories.find()
    return render_template(
        "profile.html", username=session["user"],
        image=image, recipes=recipes, categories=categories)


@app.route("/delete_account/<username>", methods=['GET', 'POST'])
def delete_account(username):
    if request.method == 'POST':
        # prevents guest users from viewing the form
        if username == session["user"]:
            user = mongo.db.users.find_one({"username": username})
            # checks if password matches existing password in database
            if check_password_hash(
                user["password"], request.form.get(
                    "confirm-password-to-delete")):
                # delete all recipes created by user
                mongo.db.recipes.delete_many({"name": session["user"]})
                # remove user from database and redirect to the home page
                mongo.db.users.delete_one({"username": session["user"]})
                flash("Your account has been deleted.")
                return redirect(
                    url_for('logout', _external=True, _scheme='https'))
            else:
                flash("Password is incorrect! Please try again")
                return redirect(
                    url_for(
                        "profile", username=session["user"],
                        _external=True, _scheme='https'))
        else:
            flash("You need to be logged in to delete your account!")
            return redirect(url_for("login", _external=True, _scheme='https'))


@app.route("/change_password/<username>", methods=['GET', 'POST'])
def change_password(username):
    if request.method == 'POST':
        # prevents guest users from viewing the form
        if username == session["user"]:
            user = mongo.db.users.find_one({"username": username})
            # Valid old password
            if check_password_hash(
                user["password"], request.form.get(
                    "old-password")):
                request.form.get("old-password")
                if {request.form.get(
                    "old-password").lower()} != {request.form.get(
                        "new-password").lower()}:
                    if {request.form.get(
                        "new-password").lower()} == {request.form.get(
                            "confirm-new-password").lower()}:
                        file_password = generate_password_hash(
                            request.form.get("new-password"))
                        mongo.db.users.update_one(
                            {"username": username},
                            {"$set": {"password": file_password}},
                            upsert=True
                        )
                        flash("Your password has been succesfully changed!")
                        return redirect(
                            url_for(
                                "profile",
                                username=session["user"],
                                _external=True, _scheme='https'))
                    else:
                        flash("Passwords Do Not Match! Please try again")
                        return redirect(
                            url_for(
                                "change_password",
                                username=session["user"],
                                _external=True, _scheme='https'))
                else:
                    flash("Your new password cannot match your old password!")
                    redirect(
                        url_for(
                            "change_password",
                            username=session["user"],
                            _external=True, _scheme='https'))
            else:
                flash("Password is incorrect! Please try again")
                return redirect(
                    url_for(
                        "change_password",
                        username=session["user"],
                        _external=True, _scheme='https'))
        else:
            flash("You need to be logged in to delete your account!")
            return redirect(url_for("login"))
    return render_template(
        "change_password.html", username=session["user"],
        _external=True, _scheme='https')


# Upload an image   Copied from Double Shamrock Hackathon and modified
@app.route("/upload_profile_image/<username>", methods=["GET", "POST"])
def upload_profile_image(username):
    if request.method == 'POST':
        for user_image in request.files.getlist("user_image"):
            # create file name for image prior to load in cloudinary
            filename = secure_filename(user_image.filename)
            filename, file_extension = os.path.splitext(filename)
            public_id_image = (username + '_' + filename)
            cloudinary.uploader.unsigned_upload(
                user_image, "profile_images",
                cloud_name='dyxuve4pr',
                folder='favourite_recipes/profile_images/',
                public_id=public_id_image)

            image_url = (
                "https://res.cloudinary.com/dyxuve4pr/image/upload/v1617292557/favourite_recipes/profile_images/"
                + public_id_image + file_extension)
            mongo.db.users.update(
                {"username": username},
                {"$set": {"image": image_url}})
        return redirect(
            url_for(
                'profile', username=session["user"],
                _external=True, _scheme='https'))
    return render_template("profile.html", username=session["user"])


# Upload an image   Copied from Double Shamrock Hackathon and modified
@app.route("/upload_recipe_image/<recipe_id>", methods=["GET", "POST"])
def upload_recipe_image(recipe_id):
    if request.method == 'POST':
        for recipe_image in request.files.getlist("recipe_image"):
            # create file name for image prior to load in cloudinary
            filename = secure_filename(recipe_image.filename)
            filename, file_extension = os.path.splitext(filename)
            public_id_image = (session["user"] + '_' + filename)
            cloudinary.uploader.unsigned_upload(
                recipe_image, "recipe_images",
                cloud_name='dyxuve4pr',
                folder='favourite_recipes/recipe_images/',
                public_id=public_id_image)
            image_url = (
                "https://res.cloudinary.com/dyxuve4pr/image/upload/v1617292557/favourite_recipes/recipe_images/"
                + public_id_image + file_extension)
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        categories = mongo.db.categories.find()
        recipe = mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)},
            {"$set": {"image": image_url}},
            upsert=True
        )
        return redirect(
            url_for(
                'edit_recipe', recipe_id=recipe_id,
                _external=True, _scheme='https'))
    categories = mongo.db.categories.find()
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        'update_recipe.html', recipe_id=recipe_id,
        recipe=recipe, categories=categories)


# Upload an image   Copied from Double Shamrock Hackathon and modified
@app.route("/upload_new_recipe_image", methods=["GET", "POST"])
def upload_new_recipe_image():
    if request.method == 'POST':
        for recipe_image in request.files.getlist("recipe_image"):
            # create file name for image prior to load in cloudinary
            filename = secure_filename(recipe_image.filename)
            filename, file_extension = os.path.splitext(filename)
            public_id_image = (session["user"] + '_' + filename)
            cloudinary.uploader.unsigned_upload(
                recipe_image, "recipe_images",
                cloud_name='dyxuve4pr',
                folder='favourite_recipes/recipe_images/',
                public_id=public_id_image)
            image_url = (
                "https://res.cloudinary.com/dyxuve4pr/image/upload/v1617292557/favourite_recipes/recipe_images/"
                + public_id_image + file_extension)
        recipe_image = {"image": image_url}
        mongo.db.recipes.insert_one(recipe_image)
        categories = mongo.db.categories.find()
        recipe_id = mongo.db.recipes.find_one({"image": image_url})["_id"]
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        'add_recipe.html', recipe=recipe, categories=categories)


@app.route("/get_categories")
def get_categories():
    if session["user"] == "admin":
        categories = list(mongo.db.categories.find().sort("category", 1))
    else:
        categories = list(
            mongo.db.categories.find(
                {"name": session["user"]}).sort("category", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        new_category = request.form.get("category")
        exists = mongo.db.categories.find_one({"category": new_category})
        if exists:
            flash("Category Already Exists")
            return redirect(
                url_for("add_category", _external=True, _scheme='https'))
        else:
            category = {
                "category": request.form.get("category"),
                "name": session["user"],
                "date": datetime.now()
            }
            mongo.db.categories.insert_one(category)
            flash("New Category Added")
            return redirect(
                url_for("get_categories", _external=True, _scheme='https'))
    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category": request.form.get("category"),
            "name": session["user"],
            "date": datetime.now()
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(
            url_for("get_categories", _external=True, _scheme='https'))
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template(
        "update_category.html",
        category=category, category_id=category_id)


@app.route("/delete_category/<category_id>/<category>", methods=['GET', 'POST'])
def delete_category(category_id, category):
    if request.method == 'POST':
        # prevents guest users from viewing the form
        if session["user"] == "admin":
            user = mongo.db.users.find_one({"username": session["user"]})
            # checks if password matches existing password in database
            if check_password_hash(
                user["password"], request.form.get(
                    "confirm-password-to-delete")):
                # delete recipe created by user
                recipes = mongo.db.recipes.find_one({"category": category})
                if recipes:
                    flash(
                        "You cannot delete this category because it is allocated to existing recipes")
                    return redirect(url_for("get_categories", _external=True, _scheme='https'))
                else:
                    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
                    flash("Category Successfully Deleted")
            else:
                flash("Password is incorrect! Please try again")
                return redirect(
                    url_for(
                        'edit_category', category_id=category_id,
                        _external=True, _scheme='https'))
        else:
            flash("You are not authorised to delete this category")
    return redirect(url_for('get_categories', _external=True, _scheme='https'))


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash("Your request has been sent")
        return redirect(url_for("contact", _external=True, _scheme='https'))
    return render_template("contact.html")


@app.route("/logout")
def logout():
    # log user out by removing user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home", _external=True, _scheme='https'))


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
