
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
6  | [Use At Home](#deploy-at-home)
7  | [Hosting](#hosting)
8  | [HabitualBe v2](#habitualbe-v2) 
9  | [Thank You's](#thank-yous)

VISIT HERE: (http://habitualbedemo.com)
Check my 2-min demo video! [`HabitualBe 2-min Demo`](https://www.youtube.com/watch?v=DQJ86Dg0IM8 "HabitualBe 2-min Demo")

## About Project and about Erikka
*Habitual be*, also called *invariant be*, is the use of an uninflected "be" in English to mark habitual or extended actions in place of the Standard English "is" and "are". 

My web app, HabitualBe, enables users to discover art both visually and via audio guided tours, and favorite them and the museums and collections they come from. 

It is my hope that other ethnic groups create repositories that are similar...for [`ethnographic research`](https://anthropology.princeton.edu/undergraduate/what-ethnography
 "Princeton definiton") and for accurate and unique "from the horse's mouth" portrayal. A less-personable version of my discovery app is [`Google Arts & Culture`](https://artsandculture.google.com/partner "Google Arts & Culture").

## Features
- `As a museum-frequenter`, I want access to a repo of museum locations, museum-specific audio guides, and curated related sounds so that my solo visits are fully immersive and more impactful.

- `As an art observer`, I'd value having my own account, favoriting art, collections, related sounds, and museums and seeing them all in one place for later reference.

- `As an art curator`, I want to view a list of museums nation-wide, collections in these museums, and related content.

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
_[List of about 70 or so museums in U.S. who have web addresses; sourced from data dump [here](https://www.imls.gov/research-evaluation/data-collection/museum-data-files] "Institute of Museum and Library Services")_ that I filtered and cleaned]

![](https://github.com/erikkaincolor/museum-app-hackbright-final/blob/main/readme-data/museum-deets-gif.gif)           
_[View museum's address and web URL and related sounds, audio guides and more]_


## Challenges

### Challenge 1️⃣ ### 
*...the favoriting feature:*
One of the major blockers I was able to overcome happened in the refinement stage. My users were unable to create, delete, or update their favorite museum, collection, audio, and art on the app.

In my code, I used the JavaScript language to send "requests" (think of these as little favors the browser wants the web app to complete successfully upon mouse-click) to my server-side code (aka the "backend" because it happens in the database part of my app that only I see).

It involves setting up an API endpoint (this is like a special door that the favors can go through to get to the backend part of the app) on the server (my server file that I wrote in Python that is) that your client-side code (the "frontend" in-browser activity) can send requests to, using a protocol such as HTTP.

Upon investigation and consulting with others, I discovered that the JavaScript API setup was not correctly committing the favoriting action to the database for logged-in users. However, with persistence, I was able to properly configure the button and persist the in-browser favoriting action to the backend using AJAX requests. This allowed the web page to update asynchronously without the need for refreshing, which improved the user experience.

### Challenge 2️⃣ ### 
*...relating all this data:*
I faced a challenge related to data retrieval and linking the different resources in my 10-table (data tables that hold user info, art info, collection info etc!) full-stack web app. To overcome this issue, I used object-relational mapping provided by SQLAlchemy to create relationships between the data using their special SQLAlchemy relationship variables.

After querying the data, I had to loop through a significant amount of content to display it on the client-side. While relating five main entities, I realized the complexity and breadth of my ambitious 10-table database. This reinforced my need for multiple join and associative tables in my model.

Overall, I used PostgreSQL, SQLAlchemy, and Python with Flask to create a complex database schema and a full-stack web application. Using ORM simplified the data retrieval and linking process for me.

## Tech Stack
`Flask` framework for my server, `SqlAlchemy` to use SQL with Python, `Python` language to power my server, `Jinja` templating for Python-esque syntax to render my HTML docs, `PostgreSQL` open source relational database so that all my data can be interconnected , `Git` for local repo, `Github` for remote repo, `Psycopg2` as a PostgreSQL database adapter for Python 

Creative: `HTML` for my page templates, `Vanilla Javascript` to power DOM manipulation and browser interactivity, `CSS` for styling, `Bootstrap5` framework


## Use At Home
If you wish to use my web app as a template for your own ethnographic museum directory for a accurate and unique "from the horse's mouth" portrayal, feel free to do so! I just ask that you tag/credit my github in your repo!

### Clone the repository
```sh
   git clone https://github.com/erikkaincolor/museum-app-hackbright-final.git
```

### Virtual Environment
Create a virtual environment to install requirements 

```sh
$ virtualenv
$ source env/bin/activate
```

### Prerequisites
Install dependencies in the requirements.txt file 

```sh
pip3 install -r requirements.txt
```

### Run Server 
```sh
python3 server.py
```

Open `http://localhost:5005` to start playing around! 

<!--
#Prerequisites 

I recommend installing yarn to make your life a whole lot easier.

* npm
  ```sh
  npm install npm@latest -g
  ```

Install the dependencies with ```yarn install```

* yarn
  ```sh
  npm install --global yarn
  ```

```virtualenv venv```

```source venv/bin/activate```

```pip install -r requirements.txt```

Run the development server with ```yarn dev```

-->
## Hosting
*Coming soon!* I’m hosting my Flask app on AWS cloud server and I picked up some handy UNIX shell commands along the way!

![Man observing art intently](https://github.com/erikkaincolor/museum-app-hackbright-final/blob/main/readme-data/md1.png "Title is optional")            
_[Man observing art intently, *Marvel Studios*]_

## HabitualBe v2
-ARIA for `accessibility`

-populate audio guides based on `geo fencing` using users location

-Implement tests (unit tests, integration tests) for `possible API usage and full-site usability for mobile`

-leverage `more open source museum and related audio info` from the web and centralize it for broader art discovery 

-`peppering salting and hashing passwords` in the case of hackers, db leaks, sql injections and angry museum admin employees 

-I want access to an `audio guide standardization proposal and mockup` 



## Acknowledgments

`A thousand thank yous to my instructors Katrina Huber-Juma, Adam Moss and our TA Katarzyna! Also to my cohortmates for checking in during project time and listening to me practice my video demo and making sure my app walkthrough was natural and user-centered. Also to the many product managers and former Hackbright women engineers who responded to my dm's, let me hold info interviews with them on Zoom and checked in with me thoughout the months ! Namely L. Quesada, V. Lorya, K. Wilks, M. Phaunef, G. Lazareva, and S. Gomez!`
