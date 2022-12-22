"This file manipulates the data in the db, saves to it, and reads/queries it via execution functions"

from model import Patron, CollectionFave, ArtFave, RelatedSoundFave, MuseumFave, Collection, RelatedSound, CollectionSound, ArtObject, Museum, connect_to_db, db

#either say .first or .all to get either one or all <----collection 
#.get would get it by key <---refer to cats demo lecture
#patron= Patron.query.get(patron_id) <---looking up by PK only bc its special, doesnt really translate to unames unique constraint

# # Manipulating an object/instance with sqlalchemy via python3 
# # creating new data, 
# # retrieving data that already exists, 
# # updating data, 
# # and deleting data.







##########CRUD FOR SEEDING
def create_patron(uname, fname, lname, email, pword): #DONE
    """create patron object 1x so seed can repeatedly"""
    patron=Patron(uname=uname, fname=fname, lname=lname, email=email, pword=pword)
    return patron
    #patron=model.Patron(uname='e', fname='ee', lname='p', email='test@test.com', pword='1234')


############################################################################################################
#                                                                                                          #
#                                       PATRONS-CRUD FOR SERVER                                            #
#                                                                                                          #
############################################################################################################









############################################################################################################
#                                                                                                          #
#                                       LOGINS-CRUD FOR SERVER                                            #
#                                                                                                          #
############################################################################################################

def patron_id_lookup(p_id): #DONE #in order to call,  id have to know id
    """get patron by id"""
    return Patron.query.get(p_id)


def patron_uname_lookup(uname): #DONE #in order to call,  id have to know uname
    """get patron by uname"""
    return Patron.query.filter(Patron.uname == uname).first()

# def create_account(uname, pword):
#     patron=Patron(uname=uname, pword=pword)
#     return patron

def create_account(uname, fname, lname, email, pword): #DONE
    """create patron object 1x so seed can repeatedly"""
    patron=Patron(uname=uname, fname=fname, lname=lname, email=email, pword=pword)
    return patron









##########CRUD FOR SEEDING
# CREATE Collection, #DONE the logic will just be that the brooklyn museum let 4 museums borrow 3 art objects per colelction.
def create_collection(coll_category, name, description, curator, era):
    """create collection object 1x so seed can repeatedly"""
    collection= Collection(coll_category=coll_category,name=name,description=description,curator=curator, era=era)
    return collection
#in seed, will have 3 art obj each, create crud for that? or attach via hardcode


############################################################################################################
#                                                                                                          #
#                                   COLLECTIONS-CRUD FOR SERVER                                            #
#                                                                                                          #
############################################################################################################

def get_collections(): #DONE
    """read all collection data..collections that ill for loop through in jinja once i pass it into view func""" 
    return Collection.query.all()

def get_collection_id(id): #DONE
    """read all collection data..collections that ill for loop through in jinja once i pass it into view func""" 
    return Collection.query.get(id)

# CONNECT CollectionSound to collection
# def marry_collection_sound(collection_id, related_sound_id):
# """relationship object"""
#     coll_sound=CollectionSound(collection_id=collection_id, related_sound_id=related_sound_id)
#     return coll_sound  

# #c1 = model.Collection(coll_category="paint",name="paintings",description="words go here",curator="someone")
# #coll_category,name,description, curator

#def get_collection_by_id(collection_id): 
#   """as a patron i want to view more info about a indiviual Collection""" 
#   art_in_collection=ArtObject.query.filter_by(ArtObject.collection_id==???)
#   result=Collection.query.get(collection_id)
#   db.session.add(result) #will mess up atomicity
#   db.session.commit() #will mess up atomicity
#   return result









##########CRUD FOR SEEDING
def create_museum(name, city, state, country, collection_id): #DONE
    """create museum object 1x so seed can repeatedly"""
    museum=Museum(name=name, city=city, state=state, country=country, collection_id=collection_id) #removed 'collection=c1'
    return museum
    #m1=model.Museum(name='Houston Museum of African American Culture', city='Houston', state='TX', country='USA') #removed 'collection=c1'

############################################################################################################
#                                                                                                          #
#                                            MUSEUM-CRUD FOR SERVER                                        #
#                                                                                                          #
############################################################################################################

def get_museums(): #DONE
    """read all museum data..collections that ill for loop through in jinja once i pass it into view func""" 
    return Museum.query.all()
    
def get_museum_by_id(id): #DONE
    """read all museum data..collections that ill for loop through in jinja once i pass it into view func""" 
    return Museum.query.get(id)
    












##########CRUD FOR SEEDING
def create_art_object(artist, title, medium, description, era, collection_id): #DONE
    """create art object 1x so seed can repeatedly"""
    art_obj=ArtObject(artist=artist, title=title, medium=medium, description=description, era=era, collection_id=collection_id) #add c3, c2
    return art_obj
# #these belong in seed and (3) are to be attached to (1) collection, so that i can attach a museum to the collection (logic: the museum i sleasing the collection)

############################################################################################################
#                                                                                                          #
#                                       ART OBJECT=CRUD FOR SERVER                                         #
#                                                                                                          #
############################################################################################################

# def get_art(): #DONE
#     """read all art object data..collections that ill for loop through in jinja once i pass it into view func""" 
#     return ArtObject.query.all()

# CONNECT ArtObject to collection-MAY NOT NEED
# def marry_collection_art_object():
# """relationship object"""
#     c1.art_object.append(a2)
#     return
#     #c1.art_object.append(a2)

#def get_art_by_id(art_id):
#   pass
#   return art_id
#   art_in_collection=ArtObject.query.filter_by(ArtObject.collection_id==???)
#   as any of these people i want to view art (in collections), filterable, toggable
#   art=ArtObject(artist, title, medium, description, collection) #add c3, c2
#   return art







##########CRUD FOR SEEDING
#def create_related_sound(medium, sound_name, description, genre, museum_id): #DONE
# """create related_sound object 1x so seed can repeatedly"""# related_sound=RelatedSound(medium=medium, sound_name=sound_name,  description=description, genre=genre, museum_id=museum_id) #add m3, m2
#   return related_sound

############################################################################################################
#                                                                                                          #
#                                       RELATED SOUNDS-CRUD FOR SERVER                                     #
#                                                                                                          #
############################################################################################################

# def get_related_sounds(): #DONE
#   """read all sound data..collections that ill for loop through in jinja once i pass it into view func""" 
#   return RelatedSound.query.all()

# CONNECT Related Sound for museum, -MAY NOT NEED
#def marry_museum_rs():
# """relationship object creation"""
#   m1.related_sound.append(sound2)    
#   return 
#   m1.related_sound.append(sound2)    
#   c1.related_sound.append(sound2)  

# def details_related_sounds(medium, sound_name, description, museum):
#   QUERY-#   """as a patron i want to view more info about a indiviual Collection's 4-5 related sounds"""
#   sounds_list=RelatedSound.query.all()
#   sound=RelatedSound(medium, sound_name, description, museum) #add m3, m2












##crud.py deals with db connections, this dunder main will connect you to the database when you run crud.py interactively
if __name__ == '__main__':
    from server import app
    with app.app_context():
        connect_to_db(app)


#FAVORTIES
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#the relation is on patron and not the faves.....via backref...so idk if i can use it correctly
# # CONNECT CollectionFave to patron
# def get_collection_fave(patron_id, collection_id)
# """relationship object"""
#     coll_fave=CollectionFave(patron_id=patron_id, collection_id=collection_id) 
#     return CollectionFave.query.filter_by(CollectionFave.perspn_id=id)
#     #patron.collection_fave.append(c1) 

#or

# # CONNECT ArtFave to patron
# def get_art_object_fave(patron_id, art_id):
# """relationship object"""
#     # art_fave=ArtFave(patron_id=patron_id,art_id=art_id) #accidentally enlisted help of fk's
#     fave=ArtFave(patron_id=patron_id, art_id=art_id)
#     # favorite=patron_id.art_fave.append(fave)
#     return ArtObjectFave.query.filter_by(ArtFave.perspn_id=id)

#or

#get help!
# def get_art_object_fave(favorite):
# # def summon_art_object_fave(art_obj, patron):
#     # art_fave=ArtFave(patron_id=patron_id,art_id=art_id) #accidentally enlisted help of fk's
#     art_fave=ArtFave(favorite=favorite) #either patron and art fk's or art_fave relationship majic var 
#     #fave=ArtFave(art_obj=art_obj, patron=patron) #either patron and art fk's or art_fave relationship majic var 
#     patron.art_fave.append(art_fave)
#     return 

# >>> rat= Rating(score=5, user=test user)
# >>> movies[0]. ratings.append(rat)
# >>> db. session. commit()

#or

# def create_rel_to_art_fave(art_obj, patron): #needed patron from somewhere
#     #patron=create_patron()
#     art_rel=patron.art_fave.append(art_obj)
#     return art_rel
# # patron.art_fave.append(a1)

#or 

# def get_favorites():
#     return ArtFave.query.get()
# # def patron_info(uname):
# #     patron = Patron.query.filter(Patron.uname == uname).first()
# #     return patron
# #get_uname function

#or 


# # # # CONNECT RelatedSoundFave to patron 
# def summon_sound_fave(patron_id, related_sound_id):
# """relationship object"""
#     sound_fave= RelatedSoundFave(patron_id=patron_id, related_sound_id=related_sound_id)
#     return RelatedSoundFave.query.filter_by(RelatedSoundFave.perspn_id=id)
# # # patron.related_sound_fave.append(sound1) 

#or 


# # # # CONNECT MuseumFave to patron
# def summon_museum_fave(patron_id,  museum_fave_id):
# """relationship object"""
#     museum_fave=MuseumFave(patron_id=patron_id,  museum_fave_id= museum_fave_id)
#     return MuseumFave.query.filter_by(MuseumFave.perspn_id=id)
# # patron.museum_fave.append(m1)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
