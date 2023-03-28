<h1 align="center">4P Juan Jose Ruiz Ruiz - A Blessed Turtle Game Studio Wiki</h1>

[View the live project here.](https://wiki-abt1.herokuapp.com/)

This page is a wiki where a fictional game studio organise information of their games, and is available to the general public so players can learn more about the worlds created by this studio.

<h2 align="center"><img src="assets/images/SimonSaysReadmeLogo.png"></h2>

<h2 align="center"><img src="assets/images/SimonHeader.png"></h2>

## User Experience (UX)

-   ### User stories

    All the user stories where created in Github issues, organised in different columns depending if they were to do, in progress or completed.

-   ### Design
    -   #### Color Scheme
        -   The colors chosen are a chromatic triad of cian, red and yellow:
        <h2 align="center"><img src="assets/images/ColorPallette.png"></h2>

    -   #### Typography
        -   The Kanit font is the only one used in this project, as it gives a similar feeling as the original Simon game font, but feels more modern and fresh.

## Features

-   Responsive on all device sizes

-   Category organised posts that can be edited by the user

-   Comment section in posts

-   Like/dislike posts

-   Contact form with input validation

-   Authentication system

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JS](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the the start and send email buttons to show the user easily where he/she can interact.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Django:](https://www.djangoproject.com/)
    - Django is the framework used to build the whole site.
1. [Heroku:](https://www.heroku.com/)
    - Heroku is the platform used to host the site.
1. [Cloudinary:](https://cloudinary.com/)
    - Cloudinary is used to manage the images in the site.
1. [ElephantSQL:](https://www.elephantsql.com/)
    - ElephantSQL is used to create and host the database for the site.
1. [Adobe Color Wheel:](https://color.adobe.com/es/create/color-wheel)
    - Adobe Color Wheel was used to create the color palette for the website.
1. [Summernote:](https://summernote.org/)
    - Summernote was used in the text fields where the user needed more styling text tools.
1. [Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Crispy Forms was used in the comment section to give it better styling.


## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
        <h2 align="center"><img src="assets/images/HTMLValidation.png"></h2>
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
        <h2 align="center"><img src="assets/images/CSSValidation.png"></h2>
-   [JSHint](https://jshint.com/)
        <h2 align="center"><img src="assets/images/JSHint.png"></h2>

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want the user to be able to understand the game and play as fast as possible.

        1. Upon entering the site, users find the name of the game, with a short description of how to play, a visible start button, and 
        2. The game takes most of the website space, so the user will not lose it.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to be able to restart the game quickly enough to not lose interest.

        1. The website checks automatically if the user chose the correct sequence or not.
        2. When the game finishes, the users just have to press the start button to try again.

-   #### Frequent User Goals

    1. As a Frequent User, I want to be able to have some way of saving history of my score.

        1. At the end of the website, the user can find a small form he can complete to get the score in his/her email.

### Further Testing

-   The Website was tested on Google Chrome, Microsoft Edge and Opera browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop and Xiaomi Redmi Note 10.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Bug Log

- When tests are executed, the console is not able to create a testing database to check the tests - 
- In the deployed project, style.css is not loading - 
- When try to access a post, the page can't load because it can't find the correct slug - Use get_absolute_url() method in the post model.
- Even when the view and url seems to be right, contact page can't load - Change the order of the contact url in urls.py
- In the contact form, it gives an error when the user try to use it to send a message - needed to create an application password in the gmail and update settings.py

## Deployment

### Heroku

The project was deployed to Heroku using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Locate the "Pages" Section in the lateral menu.
4. Under "Source", click the dropdown called "None" and select "Main Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://deneb331.github.io/2P-JuanJoseRuizRuiz-SimonSays/) in the "GitHub Pages" section.

## Credits

### Code

-   The main references used to build this website are the 'I think therefore I blog' CI project for Django references, [Writing your first Django app](https://docs.djangoproject.com/en/4.1/intro/tutorial01/), and the rest of Django documentation.

-   [Django Documentation](https://docs.djangoproject.com/en/4.1/) :  for research about forms, email features and help understanding Django workflow.

-   [W3Schools](https://www.w3schools.com/) : For research about CSS features.

-   [Stack Overflow](https://stackoverflow.com/) : For research about errors and dead-end situations.

### Content

-   All content was written by the developer, based in the projects and templates given by Code Institute, tutorship, resources found in documentation and Stack Overflow and my mentor help.

### Media

-   

### Acknowledgements

-   My Mentor for continuous helpful feedback and resources.
-   Code Institute Tutorship for help when needed.
-   The Slack community for the instant help whenever I needed it.