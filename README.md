<h1 align="center">MS4-Lettering Graphic Design E-shop</h1>

[View the live project here.](https://ms4-lettering-design-e-shop.herokuapp.com)

This is my full-stack e-commerce website built while studying Django under extremely tight deadline and I will keep on working on it after the submission deadline.

<h2 align="center"><img src=""></h2>

## Table of Contents
1. [UX](#ux)
    - [Goals](#goals)
        - [Site user Goals](#site-user-goals)
        - [Shopper Goals](#shopper-goals)
        - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
        - [Site user Stories](#site-user-stories)
        - [Shopper Stories](#shopper-stories)
        - [Business Stories](#business-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Home app](#home-app)
    - [Features Left to Implement](#features-left-to-implement)

3. [Data Schema](#data-schema)

3. [Technologies Used](#technologies-used)

4. [Testing](#testing)


5. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)

6. [Credits](#credits)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)



# User Experience (UX)
## Goals
### Site user Goals
- Browse products and view details
- easily register for an account
- easily login or logout
### Shopper Goals
- View a list of products
- View an individual product details
- personalise the product
- easily view the total of my purchases at any time
- easily select and submit the personalisation details
- view items in the shopping bag
- easily enter payment info
- feel my personal and payment info is safe and secure
- view an order confirmation after checkout
- receive and email confirmation after checkout

### Business Goals
- Add a product
- edit/update a product details
- delete a product
- offer discount for bundle purchases
- Make sure the shoppers have smooth shopping Experience

## User Stories

### Site User Stories
As a site visitor of WORD4U, I expect/need/want to:
- have a personal account to view my profile
- access my personal account info
- recover access to my account
- verify that my account registration was successful
### Shopper Stories
As a shopper of WORD4U, I expect/need/want to:
- define the color and content of the product
- avoid exceeding my budget
- ensure I receive my ideal personalisation
- identify the order and cost details before checkout,
- checkout smoothly
- confidently provide info to make a purchase
- to be able to verify the final order details
- keep the confirmation for my records
### Business Stories
As the business owner/administration, I want/need to:
- manage stock and receive orders and payments smoothly
- change product price, description, images and other product criteria
- remove products if needed

## Design Choices

Since I really appreciate the classic design of Boutique Ado from CI course, the main design is inspired from it, but I have modified the main fonts to Montserrat to deliver a more elegant visual effect.

### Colours

I used this greyish green as the theme color, to deliver a modern and clean impression, although black and white are still the main colors because the product page will be filled with colorful images.

## Wireframes

The wireframes were created using app downloaded from [Balsamiq](https://balsamiq.com/).

[home]()
[products]()
[product details]()

# Features
 
## Existing Features
- navigation bar
- personalisation form
- secure checkout through stripe, with payment confirmation
- personal profile
- customers can add/edit items in shopping bag
- register/login/logout functions with confirmation
- admin user can add/edit/remove products
- testimonies from customers can be added to homepage, and only the latest three testimonies will be shown

## Features to be developed
- a Contact page for cusomers/site visitors to contact the business
- an About page should be added to provide business information to increase credibility
- a Freebies page can be added for visitors to download some free universal designs e.g. Christmas card etc.

## Schema Design
 The schema includes these main sections/models:

**profile:** These are the details that the user saves to their profile for quick checkouts in the future. The username, email address and password details are set when the user registers for the site, and the delivery details are added when the user makes a purchase and selects to save those details to their profile.

**order:** This includes the overall order in full

**order_line_items:** This includes details of each product the user orders, the details of each product are linked to the products section including the personalisation details

**personalisation:** Including fields for customers to personalise the lettering design products

**testimonies:** For satisfied customers, the site owner is able to add their testimonies to homepage

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript]
-   [Python]

### Frameworks, Libraries & Programs Used

1. [Django](https://www.djangoproject.com/download/)
1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes] during the design process.
1. [Heroku]

## **Deployment**

### **Local**

* This project is deployed live on [**Heroku**](https://pq-the-philanthropist.herokuapp.com/).

* You can run the code in your chosen local **Integrated Development Environment** (**IDE**, e.g. [**VS Code**](https://code.visualstudio.com), [**AWS CLoud9**](https://aws.amazon.com/cloud9)).
    1. Open the **Project Repository** in [**Github**](https://github.com/an-slua-sidhe/milestone-3).
    2. Look for the green *Coded* button at the top right of the repository.
    3. If using [**Github Desktop**](https://desktop.github.com), chose to *Open in Desktop*.
    4. If you want to **Clone** the files into a **Git** repository, chose to copy the URL from the same menu (# 2.). Open your chosen **Command Line Interface** (**CLI**, e.g. [**Gitbash**](https://git-scm.com/downloads)) and use the following command:


        ``` bash
        git clone https://github.com/an-slua-sidhe/milestone-3.git
        ```

    5. To set up the files manually in a local repository, chose to **Download ZIP** and remove the files from the ZIP folder. Place them into the chosen location. If desired, set up a **Git** repository in this folder in your **CLI** with the following command:

        

        ``` bash
        git init
        ```

    6. You can check the state of your repository after initialising it by using this command:

        

        ``` bash
        git status
        ```

### **Remote**

* To push the code to a remote repository, follow the steps below (I use **Github** as an example).

    1. After using the command 'git status' (see step 6 above) in the command line, check that the console reads:


        ``` bash
        Nothing to commit
        working tree clean
        ```

    2. Next, link your remote repository. For **Github**, open your Github account and select *Repositories*. At the top right of the screen select *New*.

    3. Give your repository a name. Keep it short and avoid underscores.

    4. You can now choose a few different ways to link the local and remote repositories. The one we want here is "…*or push an existing repository from the command line*". Copy the code this option gives you and paste it into your command line. It should look something like this:

        ``` bash
        git remote add origin https://github.com/an-slua-sidhe/milestone-2
        git push -u origin master
        ```

    5. Now you can push any changes from the command line with:

        ``` bash
        git push
        ```

    6. If you check the status of of your local repository now (using 'git status') it should give you something like this:

        ``` bash
        On branch master
        Your branch is up-to-date with 'origin/master'.
        nothing to commit, working tree clean
        ```

    7. Finally, to deploy the code live with **Github Pages**, open the repository in your **Github** account and select '*Settings*' at the top right of the page. Scroll down to the *Github Pages* section. Click on the '*None*' button. Select the correct branch from the menu. Now click on the URL link to visit the deployed site.

### **Heroku**

* To push the code to a Heroku and deploy it dynamically, follow the steps below.

    1. Following on from **Local** deployment step 6 above, type the command 'git status' in the command line and check that the console reads:

        ``` bash
        Nothing to commit
        working tree clean
        ```

    2. Next, create an App on Heroku. Log in to your previous Heroku account or set up a new one, select the *New* button on the top right of the screen, then select *Create New App*.

    3. Name your app (usinb only lowercase characters and dashes) and choose the regional server that best suits your location.

    4. Next, login to your Heroku account from your CLI using:

        ``` bash
        heroku login
        ```

        A browser window should open up where you can click to login to your account through your local IDE. If this does not open, select the link on the CLI with *ctrl + c* and open it manually.

    5. Link your existing Git repository to Heroku by adding Heroku as a remote repository:


        ``` bash
        heroku git:remote -a <project-name>
        ```

    6. From now on you can push your code from the CLI with:

        ``` bash
        git push heroku master
        ```

    7. Set the necessary *Environment Variables*. Select the *Settings* tab, and then select the *Config Vars* button. Enter the KEY - VALUE pairs for your config variables here (e.g. SECRET_KEY, IP, PORT etc.)

    8. Finally, select the *Open App* button the top right of the screen to see your deployed application.


## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

### Testing User Stories from User Experience (UX) Section

- Site users are able to :
    - Browse products and view details
    - easily register for an account
    - easily login or logout
- Shoppers are able to:
    - View a list of products
    - View an individual product details
    - personalise the product
    - easily view the total of my purchases at any time
    - easily select and submit the personalisation details
    - view items in the shopping bag
    - easily enter payment info
    - feel my personal and payment info is safe and secure
    - view an order confirmation after checkout 
- Business owner/admin is able to:
    - manage stock and receive orders and payments smoothly
    - change product price, description, images and other product criteria
    - remove products if needed

### Existing Problems
- App responsiveness Problems on mobile devices including iphone8 plus etc.
    - shopping bag page not shown properly hence unable to checkout on mobile
- Code not fully tidied up throughout
- Typos in webpage contents

### Languages
- This project uses HTML, CSS, JavaScript and Python programming languages.

## Code

- Project code inspired from [Boutique Ado course material](https://github.com/ckz8780/boutique_ado_v1/tree/a07c1ca5a3b973eb47e5c944829cea06ead3936d)

# Media
- All products images are from [FreeFonts](https://fontbundles.net/free-fonts)
