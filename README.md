<h1 align="center">
Milestone Project 3 - SocialEyes - David O Neill
</h1>

<h1 align="center"> 
<img src="/static/images/small-logo.png" width = "100px" alt="logo">
</h1>

<h2 align="center"><a href="http://socialeyes-ie.herokuapp.com/">Visit SocialEyes</a></h2>

<h4 align="center"> About SocialEyes </h4>
SocialEyes is a social media platform designed to encourage people to think about and discuss information they read. Whether it's a video, a news article, an instagram post, a research paper, or a podcast, SocialEyes gives people a platform to share their thoughts about the topic of their choice.    
             
<h4 align="center"> What makes SocialEyes different?</h4>
SocialEyes is designed differently than most social media media. While most, such as Facebook or Twitter, encourage 
quantity, we enourage quality. We hope to achieve this with a number of features:

 - No comments! Unlike other social media sites, we want the discussions to happen offline. See an article and opinion you
 find interesting? Show it to your partner and chat about it! We hope this feature will encourage more conversation and reduce 'trolling' and 'keyboard warrior' type behaviour.
            
- Only your latest post will show on your followers feed. Make each post count!
        
- You must provide a link to the content you are discussing. Our aim is to add credibility to posts and allows other users to form opinions alongside yours!


## Contents

1. [**UX**](#ux)
   - [**Strategy**](#strategy)
   - [**Scope**](#scope)
   - [**Structure**](#structure)
   - [**Design**](#design)
   - [**Surface**](#surface)

2. [**Features**](#features)
    - [**Features Implemented**](#Features-Implemented)
    - [**Possible Future Features**](#Possible-Future-Features)

3. [**Technologies Used**](#technologies-used)
    - [**Languages Used**](#Languages-Used)
    - [**Libraries Used**](#Libraries-Used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)

## UX

### [**Strategy**](#strategy)

In this section, we need to develop the business goals, target audiences, and most
importantly the value our website/app will add for the user.

#### Business Goals

In terms of business goals, our social media site in theory can be developed into a space where advertisers and brands can 
spread their message to a targeted audience. SocialEyes can build a large database of users seperated into communities based on interests.

#### User Goals

- Learn more about what's happening in the world 
- Share their opinion and learn other's opinions on topics 
- Discover new points of view 
- Stay informed 

#### Target Audience

We must conisder how our audience might incluence our design (both visually and technically)
Our taget audience for this app is very wide (Roughtly: 18-50). Therefore, we need to make sure our application is designed with
encorporate all users that may land on our website. To do this, we can make sure:

- Our visual design is young enough not to be boring but also easily understood by an older audience
- Our app must be simple to use for all audiences

### [**Scope**](#scope)

In this section, we will discuss how features will align with our strategy. We need to identify what needs to be done, what tradeoffs we might need to make, 
and ask ourselves more about the user and their journey using our app. We will discuss the needs of the user.

#### What is the user looking for? 
Our user is looking for somewhere they can share opinions about what is happening around them, learn new points of view, follow
the thoughts of people they know, and stay informed. 

 
#### What the user might not know they need? 
From time to time, users might feel some content should not be on the platform 
To address this, we will need to include a way for users to 'object' or 'report' posts for review. 

### [**Structure**](#structure)

This section is concerned with how the content of the website will be organised. It will place structure on the user 
journey and make structural decisions based on our Strategy and Scope.

### Navigation

In terms of navigation, we need to ensure that getting around the site is easy and intuitive. 

The site will be divided into four sections 
- Dashboard 
- Follow/Find People 
- News 
- Settings 

The main menu will be fixed to the bottom of the page allowing the user to easily navigate between sections. 

We will also include intuitive navigation into our site: 
- When a user clicks on an avatar, it will take them to that users profile. 
- When the user clicks on their own avatar in the profile section, it will allow them to edit it
- When the user clicks on the about me section, it will allow them to update it 


### Feedback & Safety 

The user needs to feel safe throughout the experience and receive feedback for their actions. 

To do this we can include:
- Buttons change colour when interacted with 
- If the user types in a non-existant sub-directory, they will be given feedback and a link back to safety.
- Form validation will be clear and provide the necessary feedback to the user


### [**Design**](#design)

This section is concerned with how things might look and most importantly how we can give form (visual design) to function. 
We must remember that function and value is what is important and it should influence every design decision that is made.
 
Our goal with design is two fold
 - Rapidly establish value for the user
 - Lead and encourage the user to continue their experience

Our design must
 - Be audience appropriate
 - Meet the needs of the intended audience

Things to remember
 - Too many choices leads to confusion (too few leads to lack of customisation)
 - Minimum but effective design is key
 - Use conventions that people are used to (don’t change it unless it really adds more value)

 #### Register / Login (Landing Page)

<img src="/wireframes/landing-desktop.png" width ="300px" alt="landing-page-wireframe">

1.
- Function: It should be immediately obvious to the user what steps they can take in order to contintue their experience.
- Form: We will include a large and visually ovious 'Play Now' option as the most obious next step in the user experience 

2.
 - Function - The purpose of the site/app should be immediately obvious 
 - Form - We can include a logo and a title that matches the purpose of the game (Guess that Title / Think you know your movies?)
3.
 - Function: There should be a 'safety' option immediately obious to the user on landing if they don't understand what the site is about 
 - Form: We can include a large and easy to access 'How to Play' button on the landing page 

 4.
 - Function: The user should have an option to explore, learn more, and contact us
 - Form: We will include a collapsing menu that the user can use to access these functions 


 #### How To Play

<img src="readme-images/how-to-play-wire.png" width ="300px" alt="how-to-play-wireframe">

1. 
- Function: The user should be able to see an easy to read, visually appealing set of instructions that will provide them with all necessary
information to play the game 
- Form: We can include visual instructions for the two key steps in playing the game (Choosing a theme and guessing a title). We can also include 
information on how many lives the user will have and under what terms they will lose a life. 

2. 
- Function: After reading the instructions, it should be very easy to take the next step and play the game 
- Form: We can include a Play Now button at the end of the instructions so the user can easily access the game 

#### Learn More 

<img src="readme-images/learn-more-wire.png" width ="300px" alt="learn-more-wireframe">

1. 
- Function: The user should be easily able to learn the basics of how the app works and the story behind it 
- Form: We can include information and a link to the OMDB API used by the app. We can also describe the languages used to build the app. 

2. 
- Function: The user should be able to contact the developer if they have any further questions 
- Form: We can include a contact us form that allows the user to send us an email

#### Display Questions 

<img src="readme-images/display-question-wireframe.png" width ="300px" alt="display-question-wireframe">

1. 
- Function: The user should be able to view the question easily and know how to answer it 
- Form: We will display the question in a large font size and include a placeholder 'Type Answer Here' in the html input box 

2. 
- Function: The user should be able to see what question they are on and have many lives they have 
- Form: We will include a question counter and a lives counter in the top left and right hand of the screen 

3. 
- Function: The user should be able to skip a question if they don't know the answer 
- Form: We will include a Skip Question button just under the answer section 

4. 
<img src="readme-images/loading-wire.png" width ="100px" alt="loading-wireframe">

- Function: We must retrive the content from the API before display the questions to the user 
- Form: We will include a loading GIF that will run until all the information is restrived from the API. This will allow for the 
smoother user experience.


### [**Surface**](#surface)

This section is concerned with Typography, Color schemes, imagery, and brand identity 

#### Typography 
/*------ */

#### Colour Scheme
/*------ */

#### Copy 
/*------ */

### Wireframes 

/*------ */


## FEATURES

## Features-Implemented

/*------ */


## Possible Future Features
/*------ */


## Technologies Used 

## Languages Used 

HTML5, CSS3, Javascript, Python  

### Libraries Used
* <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask </a>
* <a href="https://getbootstrap.com/">Bootstrap 4 </a>
* <a href="https://jquery.com/">JQuery </a> - DOM manupulation
* <a href="https://www.mongodb.com/">MongoDB</a> - Database 
* <a href="https://www.npmjs.com/package/bcrypt">Bcrypt</a> - Used for password encryption 
* <a href="https://pymongo.readthedocs.io/en/stable/"> PyMongo</a> - Used to connect to MongoDB using python
* <a href="https://fontawesome.com/">Font Awesome </a> -Icons 
* <a href="https://fonts.google.com/">Google Fonts</a> - Typeography 
* <a href="https://github.com/">GitHub</a> - Used for version control and code hosting - Github pages used to host the final version of the game
* <a href="https://gitpod.io/">GitPod</a> - Used as an online IDE


## Testing 

Testing was carried out in a number of ways for this site. 

#### General Site Tests 
 - All interactive elements were checked first. On Desktop, any hover effects/color changes  
were checked (social media links). On mobile, the same effects were checked when links were clicked. 

 - Every link on the page was checked to ensure that it directed the user to the correct page. Every button was clicked and checked that 
it directed the user to the correct page.

 - Any links that activated popups were checked that they functioned correctly. All popups were checked to see if the 
'close' buttons function correctly. 

 - The site was then tested on multiple screen sizes and orientations (horizontal & vertical) using Chrome Developer Tools. 
All text was checked to make sure it was easily readible on any screen size. Item spacing was checked to make sure there was sufficient spacing between all elements on all screen sizes.


#### User Testing


#### Code Validation 
- HTML code was ran though a HTML validator to ensure there were no errors (https://validator.w3.org/#validate_by_input)
- CSS code was ran though a CSS validator to ensure there were no errors (https://jigsaw.w3.org/css-validator/#validate_by_input)

#### Jasmine Testing 



#### Beta Testing 



## Deployment 

* I used git init to initialise a local repository. 
* I used git add . - to add the base directory of project code into the local git repository 
* I used git commit -m ".." to commit to the local repository with a message containing information on the version 
* I used git push to push the local repository to the remote repositiry on GitHub

I took the following steps to deploy me project. 

1. 
2. 
3. 
4. 
5. 


## Credits 
