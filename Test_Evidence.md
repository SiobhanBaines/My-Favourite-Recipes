# My Favourite Recipes Test Evidence
## Unit and Functional Testing

####    Navigation
The navigation bar needs to work consistently across all pages. It needs to take the website user to where they want to go and where the label says. The layout of the navigation bar needs to be clean, easily understood and consistant across the site. On medium and small devices the inital navigation bar appears as the 'hamburger' icon which, when clicked produces the navigation down the side of the screen. When the side navigation is clicked again it will disappear.
#####   Nav Bar on Large Devices
 ![image](static/documentation_files/images/unit_testing_images/nav_bar_large.png)
#####   Nav Bar on Medium Devices
 ![image](static/documentation_files/images/unit_testing_images/nav_bar_medium.png)
#####   Nav Bar on Small Devices
 ![image](static/documentation_files/images/unit_testing_images/nav_bar_small.png)
#####   Nav Sidebar on Medium Devices
 ![image](static/documentation_files/images/unit_testing_images/nav_side_bar_meduim.png)
#####   Nav Sidebar on Small Devices
 ![image](static/documentation_files/images/unit_testing_images/nav_side_bar_small.png)

Each of the navigation links takes the webiste user to the relavent pages.

####    Footer
The footer allows for the addition of information and links to sites that are not directly part of this site. The website user can find information about the creator of this site. In the real world these links would be for other company information. The website user has access to be able to contact the owner of the site. The link for the weights and measure takes the website user to the BBC Good Food unit conversion page. For a corporate site it would be preferable to completely recreat this information and not link to outside the site.

#####   Footer on Large Devices
 ![image](static/documentation_files/images/unit_testing_images/footer_larger.png)
#####   Footer on Medium Devices
 ![image](static/documentation_files/images/unit_testing_images/footer_medium.png)
#####   Footer on Small Devices
 ![image](static/documentation_files/images/unit_testing_images/footer_small.png)
####    Github
The link to Github opens in a seperate window.
 ![image](static/documentation_files/images/unit_testing_images/github.png)
####    LinkedIn
The link to LinkedIn opens in a seperate window.
 ![image](static/documentation_files/images/unit_testing_images/linkedin.png)
####    Facebook
The link to Facebook opens in a seperate window.
 ![image](static/documentation_files/images/unit_testing_images/facebook.png)
####    Instagram
The link to Instagram opens in a seperate window.
 ![image](static/documentation_files/images/unit_testing_images/instagram.png)
####    Twitter
The link to Twitter opens in a seperate window.
 ![image](static/documentation_files/images/unit_testing_images/twitter.png)
#####   Weights and Measures link
This links to an external website [BBC Good Food](https://www.bbcgoodfood.com/conversion-guides). To create this within my site would have been creating a full website so I decided to simply create the link.
######  Large Devices
 ![image](static/documentation_files/images/unit_testing_images/w&m_large.png)
######  Medium Devices
 ![image](static/documentation_files/images/unit_testing_images/w&m_medium.png)
######  Small Devices
 ![image](static/documentation_files/images/unit_testing_images/w&m_small.png)

####    Home Page
#####   Home Page Large
There is a strange issue with the home page where by when the site is opened on a desktop and all navigation is done on that resolution the navigation bar fits the whole window and there is no horizontal scroll bar.
 ![image](static/documentation_files/images/unit_testing_images/home_large.png)
If the same page is inspected using DevTools and then DevTools is closed a horizontall scroll bar appears.
 ![image](static/documentation_files/images/unit_testing_images/home_large_issue.png)
To fix the issue I had to ass some styling for the .nav-extended class to force the bar to being the full width and then had to add some padding to the right of the ul element so that all them navigation options were still visible.

#####   Home Page Medium
 ![image](static/documentation_files/images/unit_testing_images/home_medium.png)
#####   Home Page Small
There is an issue when moving between device sizes where the home page, parallax image does not cover the whole of the container.
 ![image](static/documentation_files/images/unit_testing_images/home_small_issue.png)
I tried to fix this by removing some of the CSS styling for the .parallax-container class so that it only contained the overlay to lighten the image which enabled the materialize CSS. Although this looked like it worked initially, when I reloaded and ran some more tests the issue stayed the same
######  Parallax Materialize Issue
After much investigation I have come to the conclusion this is an intermittent issue with the materializecss styling for the parallax class. I thought it was related to the carousel I have on top of the background image but found I have the same issue on other pages where there is no background image. something happens to change the element.style but I have not been able to uncover the exact issue.
 ![image](static/documentation_files/images/unit_testing_images/home_parallax_image_styling.png)
 ![image](static/documentation_files/images/unit_testing_images/parallax_issue_after_refresh.png)
 ![image](static/documentation_files/images/unit_testing_images/parallax_issue.png)
 ![image](static/documentation_files/images/unit_testing_images/home_carousel_styling.png)
 ![image](static/documentation_files/images/unit_testing_images/add_category_parallax_styling.png)

####    About Page
The about page has no functionality to test but the format for UX needs to be validated across all device sizes.
There is an issue with white space on either side of the about container.
 ![image](static/documentation_files/images/unit_testing_images/about_large_issue.png) 
This issue occured because the class container is a materialize class which has a set width that is smaller than the full view width of a screen. By changing the classes from .container .about to .container-about in both the HTML and CSS the issue is resolved.
#####   About Page Large
 ![image](static/documentation_files/images/unit_testing_images/about_large_fixed.png)
#####   About Page Medium
 ![image](static/documentation_files/images/unit_testing_images/about_medium.png)
#####   About Page Small
 ![image](static/documentation_files/images/unit_testing_images/about_small.png)

####    Getting Started Page
The getting started page has one button which allows the website user to register with the site to allow them to add their own recipes. This button works.
#####   Getting Started Large
 ![image](static/documentation_files/images/unit_testing_images/getting_started_large.png)
#####   Getting Started Medium
 ![image](static/documentation_files/images/unit_testing_images/getting_started_medium.png)
#####   Getting Started Small
 ![image](static/documentation_files/images/unit_testing_images/getting_started_small.png)

####    Recipes Page
The recipe page will grow in length as more recipes are added. Clicking on one of the recipe cards will take the website user to the recipe detail page. Each recipe shows how many people have liked or disliked each recipe. 
#####   Recipes Page Large
 ![image](static/documentation_files/images/unit_testing_images/recipes_page_large.png)
#####   Recipes Page Medium
 ![image](static/documentation_files/images/unit_testing_images/recipes_page_medium.png)
#####   Recipes Page Small
 ![image](static/documentation_files/images/unit_testing_images/recipes_page_small.png)
**Issues**
1. When an image is uploaded it will need to be resized so that when it is displayed the image does not pull out of shape.
2. If there is no image a default image is needed and the recipe title font colour will need to darken.
**Resolutions**
1. Using google to search for resizing of images using Python I found [auth0.com](https://auth0.com/blog/image-processing-in-python-with-pillow/#Resizing-Images)
2. Added default image code to HTML and added a new class with CSS to change the recipe title from white to brown so that it can be read.
 ![image](static/documentation_files/images/unit_testing_images/recipe_card_default_image.png)
####    Register Page
The website user needs to register to be able to add any new recipes or categories which they will subsequently be able to read, change or delete later. (investigate - being able to stop user deleting categories used by other recipes) 
1. The individual needs to decide on a username and password. Both can consist of upper and lowercase letters and numbers and must be between 5 and 15 characters in length. 
If the username is too short the entry line changes to red and when the cursor is hovered over the line the message "Please match the requested format." appears. 
* Here the username is too short
![image](static/documentation_files/images/unit_testing_images/name_too_short.png)
* Here the user wanted to use special characters which are not allowed.
![image](static/documentation_files/images/unit_testing_images/name_special_chars.png.jpg)
* The user has entered a valid username and the HTML formating has stopped the user entering more than 15 characters.
![image](static/documentation_files/images/unit_testing_images/valid_username.png)
* If the user selects a username that already exists the receive a flash message
![image](static/documentation_files/images/unit_testing_images/username_already_exists.png)
2. Both passwords must be identical. 
* Here the passwords do not match and a flash message is displayed.
![image](static/documentation_files/images/unit_testing_images/passwords_do_no_match.png)
3. If a user already has an account they can click the link to take them to the log-in page.
![image](static/documentation_files/images/unit_testing_images/login_from_registration.png)
4. When the website visitor creates a valid username and password, the password in encrypted using Flask Werkzeug security, a record is added to the user collection in MongoDB and the user is taken to their profile page.
* MongoDB record
![image](static/documentation_files/images/unit_testing_images/mongodb_user.png)
* Profile page of a new account
![image](static/documentation_files/images/unit_testing_images/valid_registration.png)
#####   Register Page Large
 ![image](static/documentation_files/images/unit_testing_images/register_large.png)
#####   Register Page Medium
 ![image](static/documentation_files/images/unit_testing_images/register_medium.png)
#####   Register Page Small
 ![image](static/documentation_files/images/unit_testing_images/register_small.png)

####    Log-in Page
Once the website user has an account they can log in and out whenever they need.
1. The username and password are validated against the user collection in MongoDB to confirm the username exists and its password is correct.
* If the user enters either an invalid username or incorrect password a flash message is displayed. The same message is displayed for both errors to help prevent hacking.
![image](static/documentation_files/images/unit_testing_images/invalid_login.png)
3. If a user is not register there is a link to the registration page.
![image](static/documentation_files/images/unit_testing_images/register_from_login.PNG)
#####   Log-in Page Large
 ![image](static/documentation_files/images/unit_testing_images/login_large.png)
#####   Log-in Page Medium
 ![image](static/documentation_files/images/unit_testing_images/login_medium.png)
#####   Log-in Page Small
 ![image](static/documentation_files/images/unit_testing_images/login_small.png)
####    Log-out
![image]()
###     Profile Page
Below is an image of the profile page for a new user which shows a message saying they have not added any recipes and has a place to upload an image of themselves if they want to.
![image](static/documentation_files/images/unit_testing_images/new_user_profile.png)
**Issues**
The text on the buttons on the profile card are truncated.
**Resolution**
I increased the button width from 12rem to 14rem.
From this page a website user can change their password, delete their account (which will delete all the recipes they have created), add a new recipe, maintain categories. When the website user has added some recipes a table is displayed detailing the recipes they have added. Clicking on the recipe name will take them to a read-only view of the recipe or they can click on the maintain recipe button to change or delete the recipe.

#####   Profile Page Large
 ![image](static/documentation_files/images/unit_testing_images/profile_large.PNG)
#####   Profile Page Medium
 ![image](static/documentation_files/images/unit_testing_images/profile_large.PNG)
#####   Profile Page Small
 ![image](static/documentation_files/images/unit_testing_images/profile_small.png)

####    Display Recipe Page
#####   Display Recipe Page Large
 ![image]()
#####   Display Recipe Page Medium
 ![image]()
#####   Display Recipe Page Small
 ![image]()

####    Add Recipe Page
#####   Add Recipe Page Large
 ![image]()
#####   Add Recipe Page Medium
 ![image]()
#####   Add Recipe Page Small
 ![image]()

####    Edit Recipe Page
#####   Edit Recipe Page Large
 ![image]()
#####   Edit Recipe Page Medium
 ![image]()
#####   Edit Recipe Page Small
 ![image]()

####    Add Category Page
#####   Add Category Page Large
 ![image]()
#####   Add Category Page Medium
 ![image]()
#####   Add Category Page Small
 ![image]()

####    Edit Category Page
#####   Edit Category Page Large
 ![image]()
#####   Edit Category Page Medium
 ![image]()
#####   Edit Category Page Small
 ![image]()

####    Contact Us Page


 ![image](static/documentation_files/images/unit_testing_images/test_contact_us.png)

 ![image](static/documentation_files/images/unit_testing_images/email_received.png)

 ![image](static/documentation_files/images/unit_testing_images/email_received.png)

## Lighthouse Testing

## User Story Testing
### User Experience
######  Recipe Details
**As a** visitor, 
**I want** to find some tasty and fun recipes
**So that** I can quickly and easily bake something tasty for family and friends
**Given** a visitory is interested in baking,
**When** they visit the site and open a recipe,
**Then** the recipe should have all the information needed to create the dish and be clear and easy to follow.
######  Favourites
**As a** visitor, 
**I want** to know if other people like the recipe
**So that** I am confident I will enjoy it too
**Given** people have different likes and disklikes,
**When** eating food,
**Then** the site needs to have the ability to like or dislike the recipes and this information needs to be displayed clearly.
######  Contact
**As a** visitor, 
**I want** to be able to contact the organisation
**So that** when I have a question or something is wrong
**When** using the site,
**Then** a confirmation email should be sent to the visitor.
######  Registration/Login
**As a** visitor, 
**I want** to know my account is secure to me
**So that** I am confident noone else will be able to access my recipes
**Given** that passwords need to be create,
**When** a new account is registered,
**Then** the new password needs to be confirmed and encrypted to reduce the risk of hacking.
######  Upload Profile
**As a** visitor with an account, 
**I want** to be able to add an avitar or image of myself or change my password
**So that** I know I am on my own profile and I can keep it more secure
**Given** it will make the account more personal,
**When** on the profile page
**Then** there needs to be an upload image and change password facility on the profile page.
######  Add Recipes/Categories
**As a** visitor, 
**I want** to be able to add my own recipes and categories
**So that** I can share them with family and friends
**Given** the visitor has registed, creating a profile,
**When** login,
**Then** the visitor can create, read, update and delete recipes from a single location as well as having the ability to create, read and update categories if none of the current categories meet their requirements.
######  Upload Images
**As a** visitor, 
**I want** to be able to upload an image of my recipes
**So that** other people and I can see the product without having to read
**Given** it is easier to scan images than words,
**When** looking for a recipe,
**Then** the add and edit recipe pages need to have an upload image fascility.
######  Delete Account
**As a** visitor, 
**I want** to have the ability to delete my account and my recipes from the site
**So that** I know the site is complient with GDPR
**Given** the recipes belong to each visitor when they are loaded onto the site,
**When** they wish to close their account,
**Then** the recipes must also be delete because they could be classified as personal information.
