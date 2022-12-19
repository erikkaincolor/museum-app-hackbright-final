"This file manipulates the data in the db, saves to it, and reads/queries it via execution functions"

from model import Patron, CollectionFave, ArtFave, RelatedSoundFave, MuseumFave, Collection, RelatedSound, CollectionSound, ArtObject, Museum, connect_to_db, db

##########CRUD FOR SEEDING
# CREATE Patron
def create_patron(uname, fname, lname, email, pword):
    patron=Patron(uname=uname, fname=fname, lname=lname, email=email, pword=pword)
    return patron
    #patron=model.Patron(uname='e', fname='ee', lname='p', email='test@test.com', pword='1234')

# CREATE Collection, the logic will just be that the brooklyn museum let 4 museums borrow 3 art objects per colelction.
def create_collection(coll_category, name, description, curator, era):
    collection= Collection(coll_category=coll_category,name=name,description=description,curator=curator, era=era)
    return collection
#in seed, will have 3 art obj each, create crud for that? or attach via hardcode

# # CREATE RelatedSound, 
# def create_related_sound(medium, sound_name, description, genre, museum_id):
#     related_sound=RelatedSound(medium=medium, sound_name=sound_name,  description=description, genre=genre, museum_id=museum_id) #add m3, m2
#     return related_sound

# CREATE ArtObject
def create_art_object(artist, title, medium, description, era, collection_id):
    art_obj=ArtObject(artist=artist, title=title, medium=medium, description=description, era=era, collection_id=collection_id) #add c3, c2
    return art_obj
# #these belong in seed and (3) are to be attached to (1) collection, so that i can attach a museum to the collection (logic: the museum i sleasing the collection)

# CREATE Museum
def create_museum(name, city, state, country, collection_id):
    museum=Museum(name=name, city=city, state=state, country=country, collection_id=collection_id) #removed 'collection=c1'
    return museum
    #m1=model.Museum(name='Houston Museum of African American Culture', city='Houston', state='TX', country='USA') #removed 'collection=c1'

# CONNECT Related Sound for museum, -MAY NOT NEED
# def marry_museum_rs():
#     m1.related_sound.append(sound2)    
#     return 
#     #m1.related_sound.append(sound2)    

















































# CONNECT CollectionSound to collection
# def marry_collection_sound(collection_id, related_sound_id):
#     coll_sound=CollectionSound(collection_id=collection_id, related_sound_id=related_sound_id)
#     return coll_sound  
#     # c1.related_sound.append(sound2)  

# CONNECT ArtObject to collection-MAY NOT NEED
# def marry_collection_art_object():
#     c1.art_object.append(a2)
#     return
#     #c1.art_object.append(a2)

#the relation is on patron and not the faves.....via backref...so idk if i can use it correctly
# # CONNECT CollectionFave to patron
# def summon_collection_fave(patron_id, collection_id)
#     coll_fave=CollectionFave(patron_id=patron_id, collection_id=collection_id) 
#     return coll_fave
#     #patron.collection_fave.append(c1) 

# # CONNECT ArtFave to patron
# def summon_art_object_fave(patron_id, art_id):
#     # art_fave=ArtFave(patron_id=patron_id,art_id=art_id) #accidentally enlisted help of fk's
#     fave=ArtFave(patron_id=patron_id, art_id=art_id)
#     # favorite=patron_id.art_fave.append(fave)
#     return favorite
 

#######################
#get help!
# def summon_art_object_fave(favorite):
# # def summon_art_object_fave(art_obj, patron):
#     # art_fave=ArtFave(patron_id=patron_id,art_id=art_id) #accidentally enlisted help of fk's
#     art_fave=ArtFave(favorite=favorite) #either patron and art fk's or art_fave relationship majic var 
#     #fave=ArtFave(art_obj=art_obj, patron=patron) #either patron and art fk's or art_fave relationship majic var 
#     patron.art_fave.append(art_fave)

#     return 

# >>> rat= Rating(score=5, user=test user)
# >>> movies[0]. ratings.append(rat)
# >>> db. session. commit()
#######################

# def create_rel_to_art_fave(art_obj, patron): #needed patron from somewhere
#     #patron=create_patron()
#     art_rel=patron.art_fave.append(art_obj)
#     return art_rel
# # patron.art_fave.append(a1)

# # # # CONNECT RelatedSoundFave to patron 
# def summon_sound_fave(patron_id, related_sound_id):
#     sound_fave= RelatedSoundFave(patron_id=patron_id, related_sound_id=related_sound_id)
#     return sound_fave
# # # patron.related_sound_fave.append(sound1) 

# # # # CONNECT MuseumFave to patron
# def summon_museum_fave(patron_id,  museum_fave_id):
#     museum_fave=MuseumFave(patron_id=patron_id,  museum_fave_id= museum_fave_id)
#     return museum_fave
# # patron.museum_fave.append(m1)




































##########CRUD FOR SERVER
# def get_collection():
#     """I will gather all collection data""" 
#     #creating a collection query object that holds all 
#     # collections that ill for loop through in jinja once i pass it into view func
#     return Collection.query.all()

# #c1 = model.Collection(coll_category="paint",name="paintings",description="words go here",curator="someone")
# #coll_category,name,description, curator




# def get_collection_by_id(collection_id):
#     """as a patron i want to view more info about a indiviual Collection""" 
#     result=Collection.query.get(collection_id)
#     db.session.add(result)
#     db.session.commit()
#     return result






# def view_art(artist, title, medium, description, collection):
#     """as a patron i want to view more info about a indiviual Collection's 4-5 art objects"""
# # QUERY
# # as any of these people i want to view art (in collections), filterable, toggable
#     art=ArtObject(artist, title, medium, description, collection) #add c3, c2
#     return art







# def get_art_by_id(art_id):
#     pass
#     return art_id










# def view_related_sounds(medium, sound_name, description, collection_id):
#     """as a patron i want to view more info about a indiviual Collection's 4-5 related sounds"""
# ## QUERY
# # as an art observer i want to see a list of r sounds and hear them
#     sound=RelatedSound(medium, sound_name, description, collection_id) #add m3, m2
#     return sound








# # Manipulating an object/instance with sqlalchemy via python3 
# # creating new data, 
# # retrieving data that already exists, 
# # updating data, 
# # and deleting data.

# #create all tables in db 
# # (Step2: the R in CRUD) 
# # querying is getting us multiple objects/instances and whatever data using 
# # sqlalchemy via python3



#either say .first or .all to get either one or all <----collection 
#.get would get it by key <---refer to cats demo lecture
#patron= Patron.query.get(patron_id) <---looking up by PK only bc its special, doesnt really translate to unames unique constraint

def patron_id_lookup(patron_id): #in order to call,  id have to know id
    patron=Patron.query.filter_by(id=patron_id).first()
    return patron

def patron_uname_lookup(uname):
    # patron=Patron.query.filter_by(uname=patron.uname).first()
    patron = Patron.query.filter(Patron.uname == uname).first()
    return patron

#get_uname function





















# def view_museums(name, city, state, country):
# # QUERY
# # as an art observer i want to view a list of museums and select them and view more
#     museum=Museum(name, city, state, country) #removed 'collection=c1'
#     return museum

# def view_museums(id):
# QUERY
# as a patron i want to favorite any 4: collections, art, r sound, Museum
    #  pass

# def view_related_sounds(medium, sound_name, description, museum):
# ## QUERY
# # as an art observer i want to see a list of r sounds and hear them
#     sound=RelatedSound(medium, sound_name, description, museum) #add m3, m2
#     return sound


#need help
#real-world movie data to populate the movies table before 
#randomly generating fake users and ratings.




##crud.py deals with db connections, this dunder main will connect you to the database when you run crud.py interactively
if __name__ == '__main__':
    from server import app
    with app.app_context():
        connect_to_db(app)

    
