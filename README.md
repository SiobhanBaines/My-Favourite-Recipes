# My Favourite Recipes

## Project Outline
The purpose of this project is to build a full-stack site that allows users to manage a set of data using HTML, CSS, JavaScript, Python+Flask, MongoDB and external API's. This site is a personal recipe site where favourite recipes can be uploaded and shared with other site visitors. These recipes can be family heirlomes handed down throught the generations or new favourites found in a magazine, book, online or even recommended by a friend or family. A database will be used to hold the recipes with a search function. To be able to add recipes to the site a user will need to register and create login credentials.

 ![image](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/ami_responsivedesign.png)

[View the live project here](https://siobhanbaines.github.io/MS3-My-Favourite-Recipes/)
## Design Phase
### User Experience
1. **A new visitor to the site**
As a new visitor to the site I want to find some new recipes that other people love. I want the site to be easy to navigate, information to be easy to find and the site to be intuative. I would like to be able to create my own profile so that I can share my favourite recipes and store them in a convenient location.

2. **A regular visitor to the site**
I want to be able to see all recipes on the site, be able to add new recipes and potentially download a recipe or share it with a friend. If I decide to close my account I want the option to be able to delete the recipes I have contributed to the site.

### *Strategy*
A site where recipes can be loaded and shared by individuals creating a central repository where anyone can try something new or bake something that brings back child hood memories of being in Grandma's kitchen. The site will help remove the need for a book shelf full of cookery books. Thereby saving space, reducing clutter and creating a quick easy way to find something tastey to bake.

### *Scope*
[Project Design Mind Map](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/9f177456735fc658c3f85831a10604892c91f5da/documentation_files/recipes_mindmap.jpg)

The features to be included are
* The ability to select recipes by category
* The ability to create a profile which will allow the user to add/update their own recipes and contribute to the site
* The ability to download a recipe and/or email a recipe but only if the user has an existing profile
* If a user with a profile wishes to delete their account, the ability to decide if they want to delete their contribution

### *Structure*
How is the information structured, and is it logically grouped?
The navigation bar will change depending on the type of user visiting the site. 
Someone who does not have a profile will only be able to view the recipes and have the ability to register and login.
Someone who is already registered will 
* have the ability to see all the recipes they have created on a profile page
* have the abiltiy to add, change or delete any of the recipes they have contributed 
* have the abiltiy to delete their account 
* be able to print and/or email any of the recipes on the site

There will be the ability to select the recipes by category or for all categories. 
The categories will include 
* Fun with the children
* Tea time treat
* Special occasion
* What's for dinner
Recipes will be displayed in a card with an image of the final product. Clicking on the card will display all the ingredients, method, times, equipment etc and if the user is a registered user, the ability to download and/or email the recipes


### *Skeleton*
#### Wireframes
[Mobile Wireframs](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/9f177456735fc658c3f85831a10604892c91f5da/documentation_files/mobile.pdf)

[Tablet Wireframs](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/9f177456735fc658c3f85831a10604892c91f5da/documentation_files/tablet.pdf)

[Desktop Wireframes](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/9f177456735fc658c3f85831a10604892c91f5da/documentation_files/desktop.pdf)

[Database Schema](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/2bdec29915a3584ea1cab3a8fb8fda801c5596a0/documentation_files/recipe_db.png)
### *Surface*
I used Materialize to assist in the design of the website [Materialize](https://materializecss.com/)
I created a colour palette using the [background image](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/45776b725d8040182b7cc2d0b5f8311cd1807e4f/static/images/background.jpeg) and [icolorpalette](https://icolorpalette.com/)
finished product
styling, balance, consistency

### Features

### Media

### Technologies Used

### Credits
**icon**
![image](https://stock.adobe.com/uk/search/free?load_type=search&native_visual_search=&similar_content_id=&is_recent_search=&search_type=autosuggest&k=baking&acp=0&aco=baking&asset_id=273670969&content_id=273670969) Let's Bake motivational slogan or phrase handwritten with calligraphic font or script and decorated by mixer
By Good Studio 
**background for static pages**
![image](https://stock.adobe.com/uk/search/free?load_type=search&native_visual_search=&similar_content_id=&is_recent_search=&search_type=autosuggest&k=baking&acp=0&aco=baking&asset_id=178084081)baking ingredients
By Rawpixel.com
**background for weights & measures page**
![image](https://stock.adobe.com/uk/search/free?filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bfree_collection%5D=1&filters%5Bcontent_type%3Aimage%5D=1&filters%5Borientation%5D=vertical&k=baking&order=relevance&safe_search=1&search_type=filter-select&get_facets=1&asset_id=247706319) Rolling pin and a weighing scale
By Rawpixel.com

## Development Phase
### Logo image in Navbar
I want to use the image ![image](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/45776b725d8040182b7cc2d0b5f8311cd1807e4f/static/images/icon.jpeg) in the Navbar as a logo. When I added the image `<a href="" class="brand-logo"><img src="{{ url_for('static', filename='images/icon.jpeg') }}" alt=""></a>` it appears to cover the whole page ![image](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/45776b725d8040182b7cc2d0b5f8311cd1807e4f/documentation_files/images/navbarlogo.png) I googled *add image for icon navbar materialize* and found some code in [stackoverflow](https://stackoverflow.com/questions/51412303/materializecss-navbar-logo-image-position)which still didn't give me what I wanted but after some playing in dev tools I got the icon where I wanted it.![image](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/45776b725d8040182b7cc2d0b5f8311cd1807e4f/documentation_files/images/aftericon.PNG)
 
### Error when trying to run app from Heroku
![image](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/7a636739f6d6bd29e1e3bdd71fee70e520f5d6dc/documentation_files/images/heroku_deployed_issue.png)
I had a look on Google for the error code but found nothing. I then looked on Slack and couldn't find anything to help. In the end I contacted Tutor Support who asked me to look at my Procfile which was fine and then asked me about how it was deployed. I'm using the automatic deployment through GitHub. He then had a look and found the app wouldn't run on GitPod either and informed me there is a syntax issue in my Python code. I did do a quick commit and push last night before I could finish what I was doing because I had an online yoga class and was running out of time. The error was a missing 's' of methods.

## Testing and Deployment Phase

[Test Evidence]()

### How to deploy to Heroku
1. create the requirements.txt document in GitPod using the command `pip3 freeze --local > requirements.txt`
2. create the *Procfile* which Heroku needs to know which file runs the app and how to run it using the command `echo web: python app.py > Procfile"`. Remember to open the Procfile and remove the blank line at the bottom if one exists because it can interfere with Heroku running the app.
![image](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/master/documentation_files/images/blank_line.png)
3. In Heroku, 
    1. click on **New** and **Create new app**. 
    ![image](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/master/documentation_files/images/create_new_app.png)
    2. Create the app using lowercase letters, numbers and hyphans instead of spaces (NO special characters). Select the nearest region and click **Create app**
    ![image](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/master/documentation_files/images/create_new_app_details.png)
    3. Go to the **Deploy** tab to link Heroku to the correct GitHub repository
    ![image](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/master/documentation_files/images/link_heroku_to_github_repo.png) and click **connect**
4. Set up the configuration variables that exist in `env.py` by clicking on the **settings** tab, scroll down to **Config vars** and click on the button.
![image](https://github.com/SiobhanBaines/MS3-My-Favourite-Recipes/blob/master/documentation_files/images/config_vars.png).
5. Before clicking the deploy button make sure the `Procfile` and the `requirements.txt` files are deployed to Github
6. In Heroku click on **deploy** tab and click on **Enabled Automatic Deployment** and **Deploy**. 
7. Once it has deployed use the standard method of deploying to GitHub and this will be automatically replicated through to Heroku. 
    >git add .`    
    >git commit -m"message"`   
    >git push
    







