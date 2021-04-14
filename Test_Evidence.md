# My Favourite Recipes Test Evidence
## Unit and Functional Testing

####    Navigation
The navigation bar needs to work consistently across all pages. It needs to take the website user to where they want to go and where the label says. The layout of the navigation bar needs to be clean, easily understood and consistant across the site. On medium and small devices the inital navigation bar appears as the 'hamburger' icon which, when clicked produces the navigation down the side of the screen. When the side navigation is clicked again it will disappear.
#####   Nav Bar on Large Devices
 ![image](static/documentation_files/images/unit_testing_images/nav_bar_large.png)
#####   Nav Bar on Medium Devices
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/nav_bar_medium.png)
#####   Nav Bar on Small Devices
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/nav_bar_small.png)
#####   Nav Sidebar on Medium Devices
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/nav_side_bar_meduim.png)
#####   Nav Sidebar on Small Devices
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/nav_side_bar_small.png)

Each of the navigation links takes the webiste user to the relavent pages.

####    Footer
The footer allows for the addition of information and links to sites that are not directly part of this site. The website user can find information about the creator of this site. In the real world these links would be for other company information. The website user has access to be able to contact the owner of the site. The link for the weights and measure takes the website user to the BBC Good Food unit conversion page. For a corporate site it would be preferable to completely recreat this information and not link to outside the site.

#####   Footer on Large Devices
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/footer_larger.png)
#####   Footer on Medium Devices
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/footer_medium.png)
#####   Footer on Small Devices
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/footer_small.png)
####    Github
The link to Github opens in a seperate window.
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/github.png)
####    LinkedIn
The link to LinkedIn opens in a seperate window.
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/linkedin.png)
####    Facebook
The link to Facebook opens in a seperate window.
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/facebook.png)
####    Instagram
The link to Instagram opens in a seperate window.
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/instagram.png)
####    Twitter
The link to Twitter opens in a seperate window.
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/twitter.png)
#####   Weights and Measures link
This links to an external website [BBC Good Food](https://www.bbcgoodfood.com/conversion-guides). To create this within my site would have been creating a full website so I decided to simply create the link.
######  Large Devices
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/w&m_large.png)
######  Medium Devices
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/w&m_medium.png)
######  Small Devices
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/w&m_small.png)

####    Home Page
#####   Home Page Large
There is a strange issue with the home page where by when the site is opened on a desktop and all navigation is done on that resolution the navigation bar fits the whole window and there is no horizontal scroll bar.
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/home_large.png)
If the same page is inspected using DevTools and then DevTools is closed a horizontall scroll bar appears.
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/home_large_issue.png)
To fix the issue I had to ass some styling for the .nav-extended class to force the bar to being the full width and then had to add some padding to the right of the ul element so that all them navigation options were still visible.

#####   Home Page Medium
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/home_medium.png)
#####   Home Page Small
There is an issue when moving between device sizes where the home page, parallax image does not cover the whole of the container.
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/home_small_issue.png)
I tried to fix this by removing some of the CSS styling for the .parallax-container class so that it only contained the overlay to lighten the image which enabled the materialize CSS. Although this looked like it worked initially, when I reloaded and ran some more tests the issue stayed the same
######  Parallax Materialize Issue
After much investigation I have come to the conclusion this is an intermittent issue with the materializecss styling for the parallax class. I thought it was related to the carousel I have on top of the background image but found I have the same issue on other pages where there is no background image. something happens to change the element.style but I have not been able to uncover the exact issue.
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/home_parallax_image_styling.png)
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/parallax_issue_after_refresh.png)
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/parallax_issue.png)
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/home_carousel_styling.png)
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/add_category_parallax_styling.png)

####    About Page
The about page has no functionality to test but the format for UX needs to be validated across all device sizes.
There is an issue with white space on either side of the about container.
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/about_large_issue.png) 
This issue occured because the class container is a materialize class which has a set width that is smaller than the full view width of a screen. By changing the classes from .container .about to .container-about in both the HTML and CSS the issue is resolved.
#####   About Page Large
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/about_large_fixed.png)
#####   About Page Medium
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/about_medium.png)
#####   About Page Small
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/about_small.png)

####    Getting Started Page
The getting started page has one button which allows the website user to register with the site to allow them to add their own recipes. This button works.
#####   Getting Started Large
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/getting_started_large.png)
#####   Getting Started Medium
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/getting_started_medium.png)
#####   Getting Started Small
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/getting_started_small.png)

####    Recipes Page
The recipe page will grow in length as more recipes are added. Clicking on one of the recipe cards will take the website user to the recipe detail page. Each recipe shows how many people have liked or disliked each recipe. 

#####   Recipes Page Large
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/recipes_page_large.png)
#####   Recipes Page Medium
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/recipes_page_medium.png)
#####   Recipes Page Small
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/recipes_page_small.png)
**Issues**
1. When an image is uploaded it will need to be resized so that when it is displayed the image does not pull out of shape. (investigate)
2. If there is no image a default image is needed and the recipe title font colour will need to darken.
**Resolutions**
1. Using google to search for resizing of images using Python I found [auth0.com](https://auth0.com/blog/image-processing-in-python-with-pillow/#Resizing-Images)
2. Added default image code to HTML and added a new class with CSS to change the recipe title from white to brown so that it can be read.
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/recipe_card_default_image.png)
####    Register Page
The website user needs to register to be able to add any new recipes or categories which they will subsequently be able to read, change or delete later. (investigate - being able to stop user deleting categories used by other recipes) 
1. The individual needs to decide on a username and password. Both can consist of upper and lowercase letters and numbers and must be between 5 and 15 characters in length. 

2. Both passwords must be identical. 
3. If a user already has an account they can click the link to take them to the log-in page.
#####   Register Page Large
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/register_large.png)
#####   Register Page Medium
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/register_medium.png)
#####   Register Page Small
[!image](/workspace/MS3-My-Favourite-Recipes/static/documentation_files/images/unit_testing_images/register_small.png)
####    Log-in Page
#####   Recipes Page Large
[!image]()
#####   Recipes Page Medium
[!image]()
#####   Recipes Page Small
[!image]()
####    Log-out
####    Display Recipe Page
#####   Recipes Page Large
[!image]()
#####   Recipes Page Medium
[!image]()
#####   Recipes Page Small
[!image]()
####    Add Recipe Page
#####   Recipes Page Large
[!image]()
#####   Recipes Page Medium
[!image]()
#####   Recipes Page Small
[!image]()
####    Edit Recipe Page
#####   Recipes Page Large
[!image]()
#####   Recipes Page Medium
[!image]()
#####   Recipes Page Small
[!image]()
####    Add Category Page
#####   Recipes Page Large
[!image]()
#####   Recipes Page Medium
[!image]()
#####   Recipes Page Small
[!image]()
####    Edit Category Page
#####   Recipes Page Large
[!image]()
#####   Recipes Page Medium
[!image]()
#####   Recipes Page Small
[!image]()
####    Contact Us Page
#####   Recipes Page Large
[!image]()
#####   Recipes Page Medium
[!image]()
#####   Recipes Page Small
[!image]()

## Lighthouse Testing

## User Story Testing

