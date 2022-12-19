"This file manipulates the data in the db, saves to it, and reads/queries it via execution functions"

from model import Patron, CollectionFave, ArtFave, RelatedSoundFave, MuseumFave, Collection, RelatedSound, CollectionSound, ArtObject, Museum, connect_to_db, db

##########CRUD FOR SEEDING
# CREATE Patron
def create_patron(uname, fname, lname, email, pword):
    patron=Patron(uname=uname, fname=fname, lname=lname, email=email, pword=pword)
    return patron
    #patron=model.Patron(uname='e', fname='ee', lname='p', email='test@test.com', pword='1234')

# CREATE Collection, 
def create_collection(coll_category, name, description, curator, era, num_items):
    collection= Collection(coll_category=coll_category,name=name,description=description,curator=curator, era=era, num_items=num_items)
    return collection
    #c1 = model.Collection(coll_category="paint",name="paintings",description="words go here",curator="someone")

# CREATE RelatedSound, 
def create_related_sound(medium, sound_name, description, genre, mus_id):
    related_sound=RelatedSound(medium=medium, sound_name=sound_name,  description=description, genre=genre, mus_id=mus_id) #add m3, m2
    return related_sound
    #sound1=model.RelatedSound(medium="podcast", sound_name="7th chapel",  description="gold foil walls", museum=m1) #add m3, m2

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







# CREATE ArtObject
def create_art_object(artist, title, medium, description, era, collection_id):
    art_obj=ArtObject(artist=artist, title=title, medium=medium, description=description, era=era, collection_id=collection_id) #add c3, c2
    return art_obj
    # a5=model.ArtObject(artist="Basquiat", title="Untitled", medium="paint", description="wow", collection=c3) #add c3, c2

# CREATE Museum
def create_museum(name, city, state, country):
    museum=Museum(name=name, city=city, state=state, country=country) #removed 'collection=c1'
    return museum
    #m1=model.Museum(name='Houston Museum of African American Culture', city='Houston', state='TX', country='USA') #removed 'collection=c1'

# CONNECT Related Sound for museum, -MAY NOT NEED
# def marry_museum_rs():
#     m1.related_sound.append(sound2)    
#     return 
#     #m1.related_sound.append(sound2)    






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
















# def create_user(email, pword):
#     user=Patron(email, pword)
#     #uname='e', fname='ee', lname='p',
#     return user
# # def create_patron(uname, fname, lname, email, pword):
# #     return model.Patron(uname=uname, fname=fname, email=email, pword=pword)

# # def login(email, pword):
# # # as a patron i want to login
# #     pass
























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

    
