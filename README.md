
## ***HabitualBe*** is an audio and art-centric web app. ##

![](https://github.com/erikkaincolor/museum-app-hackbright-final/blob/main/readme-data/home-gif.gif)     

_[Landing page of HabitualBe]_


Contents  | Title
------------- | -------------
1  | [About Project and about Erikka](#about-project-and-about-erikka) 
2  | [Features](#features)
3  | [App Flow](#app-flow)
4  | [Challenges](#challenges)
5  | [Tech Stack](#tech-stack)
6  | [How to deploy at home](#how-to-deploy-at-home)
7  | [Hosting](#hosting)
8  | [HabitualBe v2](#habitualbe-v2) 

Check my 2-min demo video! [`HabitualBe 2-min Demo`](https://www.youtube.com/watch?v=DQJ86Dg0IM8 "HabitualBe 2-min Demo")

## About Project and about Erikka
*Habitual be*, also called *invariant be*, is the use of an uninflected "be" in Black and Caribbean English to mark habitual or extended actions in place of the Standard English "is" and "are". 

It is my hope that other ethnic groups create repositories that are similar...for [`ethnographic research`](https://anthropology.princeton.edu/undergraduate/what-ethnography
 "Princeton definiton") and for accurate and unique "from the horse's mouth" portrayal. A less-personable version of my discovery app is [`Google Arts & Culture`](https://artsandculture.google.com/partner "Google Arts & Culture").

I am an artist, museum-frequenter, member at *Museum of Fine Arts, Houston* and MFAH's 5A (African American Art Advisory Association) chapter. I have my B.S. in Digital Media Innovation, minor in Industrial Design and *now* am a Software Engineer interested in learning more about system architecture, product management, and the backend.

## Features
- `As a museum-frequenter`, I want access to a repo of museum locations, museum-specific audio guides, and curated related sounds so that my solo visits are fully immersive and more impactful.

- `As an art observer`, I'd value having my own account, favoriting art, collections, related sounds, and museums and seeing them all in one place for later reference.

- `As an art curator`, I want to view a list of Black museums nation-wide, collections in these museums, and related content.

- `As an artist`, I want all these app features!

## App Flow

![](https://github.com/erikkaincolor/museum-app-hackbright-final/blob/main/readme-data/login-gif.gif)           
_[Login]_

![](https://github.com/erikkaincolor/museum-app-hackbright-final/blob/main/readme-data/profile-gif.gif)           
_[View your patron profile with all your user data and favorited collections, museums, art and sounds!]._

![](https://github.com/erikkaincolor/museum-app-hackbright-final/blob/main/readme-data/collection-gif.gif)           
_[View HabitualBe and partner museum's collections]._

![](https://github.com/erikkaincolor/museum-app-hackbright-final/blob/main/readme-data/collection-deets-gif.gif)           
_[View indivivual collection details]_

![](https://github.com/erikkaincolor/museum-app-hackbright-final/blob/main/readme-data/art-object-deets-gif.gif)           
_[You can't even get close to the Mona Lisa. Here, you can view individual art objects up close and personal]_

![](https://github.com/erikkaincolor/museum-app-hackbright-final/blob/main/readme-data/museums-gif.gif)           
_[List of about 70 or so Black and African museums in U.S. who have web addresses; sourced from data dump [here](https://www.imls.gov/research-evaluation/data-collection/museum-data-files] "Institute of Museum and Library Services")_ that I filtered and cleaned]

![](https://github.com/erikkaincolor/museum-app-hackbright-final/blob/main/readme-data/museum-deets-gif.gif)           
_[View museum's address and web URL and related sounds, audio guides and more]_


## Challenges
:space_invader:.......:space_invader:.......:space_invader:
### Challenge 1 ### 
*...the favoriting feature:*
To me, getting data rendered in the browser via jinja templating, queried from the database via my flask server functions, and even transmitted from the backend to the frontend and back again…took immense trial by fire. In the end, it allowed my users to create, delete, and update their favorite museum, collection, audio and art and see it displayed on their patron profile.

### Challenge 2 ### 
*...relating all this data:*
I used ORM(object–relational mapping) to link them to each other via their special SQLAlchemy relationship  variables. After querying data, I looped through a good chunk of their content in order to display it client-side. Relating 5 main entities reinforced my need for multiple join and association tables in my model, and revealed the true complexity and breadth of my ambitious 10-table database! 

Using postgresql for my relational db made sense because my patron table is the single pillar in my web app that touches everything.




## Tech Stack
`Flask` framework for my server, `SqlAlchemy` to use SQL with Python, `Python` language to power my server, `Jinja` templating for Python-esque syntax to render my HTML docs, `PostgreSQL` open source relational database so that all my data can be interconnected , `Git` for local repo, `Github` for remote repo, `Psycopg2` as a PostgreSQL database adapter for Python 

Creative: `HTML` for my page templates, `Vanilla Javascript` to power DOM manipulation and browser interactivity, `CSS` for styling, `Bootstrap5` framework


## How to deploy at home
*Coming soon!*

![Man observing art intently](https://github.com/erikkaincolor/museum-app-hackbright-final/blob/main/readme-data/md1.png "Title is optional")            
_[Man observing art intently, *Marvel Studios*]_


## Hosting
*Coming soon!* I’m hosting my Flask app on AWS cloud server and I picked up some handy UNIX shell commands along the way!


## HabitualBe v2
-ARIA for `accessibility`

-populate audio guides based on `geo fencing` using users location

-Implement tests (unit tests, integration tests) for `possible API usage and full-site usability for mobile`

-leverage `more open source museum and related audio info` from the web and centralize it for broader art discovery 

-`peppering salting and hashing passwords` in the case of hackers, db leaks, sql injections and angry museum admin employees 

-I want access to an `audio guide standardization proposal and mockup` 




