"""Script to seed database."""

import os

os.system(f'dropdb muse --if-exists')
os.system(f'createdb muse')

# import model
from model import *
#import server

# model.connect_to_db(server.app)
model.connect_to_db(app)

# Updates the database schema
model.db.create_all()

# TODO: use create methods to add objects to database, committing
#       database sessions as needed

# # Load movie data from JSON file
# with open("data/movies.json") as f:
#     movie_data = json.loads(f.read())

# # Create movies, store them in list so we can use them
# # to create fake ratings
# movies_in_db = []
# for movie in movie_data:
#     title, overview, poster_path = (
#         movie["title"],
#         movie["overview"],
#         movie["poster_path"],
#     )
#     release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

#     db_movie = crud.create_movie(title, overview, release_date, poster_path)
#     movies_in_db.append(db_movie)

# model.db.session.add_all(movies_in_db)
# model.db.session.commit()



# patrons
test_patron=Patron(uname='e', fname='ee', lname='p', email='test@test.com', pword='1234')
test_patron1=Patron(uname='t', fname='er', lname='o', email='test1@test.com', pword='104')
test_patron2=Patron(uname='ty', fname='eri', lname='oe', email='test2@test.com', pword='109')
test_patron3=Patron(uname='tyk', fname='erik', lname='oeg', email='test3@test.com', pword='1090')

# collections
c1 = Collection(coll_category="paint",name="paintings",description="words go here",curator="someone")
c2 = Collection(coll_category="drawing",name="paintings by e",description="words go here too",curator="someone else")
c3 = Collection(coll_category="sculpture",name="paintings by r",description="words go here as well",curator="monet")
c4 = Collection(coll_category="print",name="rawr xd",description="words...."

#museums

#adding faves to different patrons
#create collectionfave records

test_patron.collection_fave.append(c1) 
test_patron1.collection_fave.append(c4) 
test_patron3.collection_fave.append(c3) 
test_patron.collection_fave.append(c1)  

test_patron1.collection_fave.append(c2) 
test_patron3.collection_fave.append(c1) 
test_patron.collection_fave.append(c1) 

test_patron2.collection_fave.append(c1) 
test_patron1.collection_fave.append(c2) 

test_patron3.collection_fave.append(c4) 
test_patron3.collection_fave.append(c2) 

#adding faves to different patrons + create artfave records

#adding faves to different patrons + create related sound fave records

#adding faves to different patrons + create museum fave records

# c1.patrons.append(patron2)
    
