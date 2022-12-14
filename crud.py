"This file manipulates the db, saves to it, and reads/queries it via execution functions"
# (Step 1: the C, U, and D in CRUD functionality) 
# Manipulating an object/instance with sqlalchemy via python3 

from model import Patron, CollectionFave, ArtFave, RelatedSoundFave, MuseumFave, Collection, RelatedSound, CollectionSound, ArtObject, Museum, connect_to_db

#create all tables in db 









# (Step2: the R in CRUD) 
# querying is getting us multiple objects/instances and whatever data using 
# sqlalchemy via python3

def create_user(name, email, password):
    pass

def login(email, pword):
# as a patron i want to login
    pass

def view_collection(id):
# as a patron i want to view a Collection (art, r sounds) 
# and possibly what museum its at
    pass
def view_art(id):
# as any of these people i want to view art (in collections), filterable, toggable
    pass

def view_related_sounds(id):
# as an art observer i want to see a list of r sounds and hear them
    pass

def view_museums(id):
# as an art observer i want to view a list of museums and select them and view more
    pass

def view_museums(id):
# as a patron i want to favorite any 4: collections, art, r sound, Museum
    pass
#need help
#real-world movie data to populate the movies table before 
#randomly generating fake users and ratings.
