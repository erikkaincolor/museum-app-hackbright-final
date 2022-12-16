"This file manipulates the data in the db, saves to it, and reads/queries it via execution functions"
# (Step 1: the C, U, and D in CRUD functionality) 
# Manipulating an object/instance with sqlalchemy via python3 

#creating new data, 
# retrieving data that already exists, 
# updating data, 
# and deleting data.

from model import Patron, CollectionFave, ArtFave, RelatedSoundFave, MuseumFave, Collection, RelatedSound, CollectionSound, ArtObject, Museum, connect_to_db, db

#create all tables in db 

# (Step2: the R in CRUD) 
# querying is getting us multiple objects/instances and whatever data using 
# sqlalchemy via python3

def create_user(email, pword):
    user=Patron(email, pword)
    #uname='e', fname='ee', lname='p',
    return user
# def create_patron(uname, fname, lname, email, pword):
#     return model.Patron(uname=uname, fname=fname, email=email, pword=pword)

# def login(email, pword):
# # as a patron i want to login
#     pass

def view_collection(coll_category,name,description, curator):
# as a patron i want to view a Collection (art, r sounds) 
# and possibly what museum its at
    collection = Collection(coll_category,name,description, curator)
    return collection

#c1 = model.Collection(coll_category="paint",name="paintings",description="words go here",curator="someone")
def get_collection_by_id(collection_id):
    result=Collection.query.get(collection_id)
    db.session.add(result)
    db.session.commit()
    return result

def view_art(artist, title, medium, description, collection):
# QUERY
# as any of these people i want to view art (in collections), filterable, toggable
    art=ArtObject(artist, title, medium, description, collection) #add c3, c2
    return art

def view_related_sounds(medium, sound_name, description, museum):
## QUERY
# as an art observer i want to see a list of r sounds and hear them
    sound=RelatedSound(medium, sound_name, description, museum) #add m3, m2
    return sound

def view_museums(name, city, state, country):
# QUERY
# as an art observer i want to view a list of museums and select them and view more
    museum=Museum(name, city, state, country) #removed 'collection=c1'
    return museum

# def view_museums(id):
# QUERY
# as a patron i want to favorite any 4: collections, art, r sound, Museum
    #  pass



#need help
#real-world movie data to populate the movies table before 
#randomly generating fake users and ratings.




##crud.py deals with db connections, this dunder main will connect you to the database when you run crud.py interactively

if __name__ == '__main__':
    from server import app
    with app.app_context():
        connect_to_db(app)
