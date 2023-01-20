"This file manipulates the data in the db, saves to it, and reads/queries it via execution functions"

from data.model import Patron, CollectionFave, ArtFave, RelatedSoundFave, MuseumFave, Collection, RelatedSound, CollectionSound, ArtObject, Museum, connect_to_db, db
#either say .first or .all to get either one or all <----collection 
#.get would get it by key <---refer to cats demo lecture
#patron= Patron.query.get(patron_id) <---looking up by PK only bc its special, doesnt really translate to unames unique constraint

# # Manipulating an object/instance with sqlalchemy via python3 
# # creating new data, 
# # retrieving data that already exists, 
# # updating data, 
# # and deleting data.









##########CRUD FOR SEEDING
#works
def create_patron(uname, fname, lname, email, pword): #DONE
    """create patron object 1x so seed can repeatedly"""
    return Patron(uname=uname, fname=fname, lname=lname, email=email, pword=pword)
    #patron=model.Patron(uname='e', fname='ee', lname='p', email='test@test.com', pword='1234')


############################################################################################################
#                                                                                                          #
#                                       PATRON FAVES-CRUD FOR SERVER                                       #
#                                                                                                          #
############################################################################################################

#----------------------------museum faves
#works
def create_museum_fave(patron_id, museum_id): #fk's to museum faves
    """create a museum favorite"""
    return MuseumFave(patron_id=patron_id, museum_id=museum_id)


# works and showing up on profile
def get_m_fave_by_pid(p_id):
    """get patrons museum fave id to show up on patrons profile"""
    return MuseumFave.query.get(patron_id_lookup(p_id)) 

#wip; CHAINING
def get_m_fave_delete(patron_id, museum_id):
    """get collectionfave by patron id and collection id via CHAINING"""
    return MuseumFave.query.filter(MuseumFave.patron_id==patron_id).filter(MuseumFave.museum_id==museum_id).first()

#----------------------------collection faves

#works
def create_collection_fave(patron_id, collection_id): #fk's to collection faves
    """create a museum favorite..seed db side and server side"""
    return CollectionFave(patron_id=patron_id, collection_id=collection_id)

#works and showing up on profile
def get_c_fave_by_pid(p_id):
    """get patrons museum fave id to show up on patrons profile"""
    return CollectionFave.query.get(patron_id_lookup(p_id)) 

#works; CHAINING
def get_c_fave_delete(patron_id, collection_id):
    """get collectionfave by patron id and collection id via CHAINING"""
    return CollectionFave.query.filter(CollectionFave.patron_id==patron_id).filter(CollectionFave.collection_id==collection_id).first()
#----------------------------art faves

#works
def create_art_fave(patron_id, art_id): #fk's to collection faves
    """create a art favorite..seed db side and server side"""
    return ArtFave(patron_id=patron_id, art_id=art_id)

#works
def get_a_fave_by_pid(p_id):
    """get patrons art fave id to show up on patrons profile"""
    return ArtFave.query.get(patron_id_lookup(p_id)) 

#works; CHAINING
def get_a_fave_delete(patron_id, art_id):
    """get artfave by patron id and art id via CHAINING"""
    return ArtFave.query.filter(ArtFave.patron_id==patron_id).filter(ArtFave.art_id==art_id).first()
#----------------------------sound faves

# works
def create_sound_fave(patron_id, related_sound_id): #fk's to collection faves
    """create a sound favorite..seed db side and server side"""
    return RelatedSoundFave(patron_id=patron_id, related_sound_id=related_sound_id)

# works
def get_s_fave_by_pid(p_id):
    """get patrons sound fave id to show up on patrons profile"""
    return RelatedSoundFave.query.get(patron_id_lookup(p_id)) 

#works; CHAINING
def get_s_fave_delete(patron_id, related_sound_id):
    """get soundfave by patron id and sound id via CHAINING"""
    return RelatedSoundFave.query.filter(RelatedSoundFave.patron_id==patron_id).filter(RelatedSoundFave.related_sound_id==related_sound_id).first()








############################################################################################################
#                                                                                                          #
#                                       LOGINS-CRUD FOR SERVER                                            #
#                                                                                                          #
############################################################################################################

#works
def patron_id_lookup(p_id): #DONE #in order to call,  id have to know id
    """get patron by id"""
    return Patron.query.get(p_id)

#works
def patron_uname_lookup(uname): #DONE #in order to call,  id have to know uname
    """get patron by uname"""
    return Patron.query.filter(Patron.uname == uname).first()

#works
def patron_email_lookup(email): #DONE #in order to call,  id have to know uname
    """get patron by uname"""
    return Patron.query.filter(Patron.email == email).first()

#works
def create_account(uname, fname, lname, email, pword): #DONE
    """create patron object 1x so seed can repeatedly"""
    return Patron(uname=uname, fname=fname, lname=lname, email=email, pword=pword)























##########CRUD FOR SEEDING
#works
def create_collection(coll_category, name, description, curator, era):
    """create collection object 1x so seed can repeatedly"""
    return Collection(coll_category=coll_category,name=name,description=description,curator=curator, era=era)

#works-hardcoded fk's
def create_collection_sound(collection_id, related_sound_id): #fk's to collection faves
    """create a collection sound..seed db side and server side"""
    return CollectionSound(collection_id=collection_id, related_sound_id=related_sound_id)

############################################################################################################
#                                                                                                          #
#                                   COLLECTIONS-CRUD FOR SERVER                                            #
#                                         + ART OBJ                                                                 #
############################################################################################################

#works
def get_collections(): 
    """read all collection data..collections that ill for loop through in jinja once i pass it into view func""" 
    return Collection.query.all()

#works
def get_collection_id(id): #DONE
    """read all collection data..collections that ill for loop through in jinja once i pass it into view func""" 
    return Collection.query.get(id)

############################################################################################################

#works-hardcoded fk's
def get_art_by_coll_id(collection_id): #collection_id is passed in via route
    """artobj via collectionid to show all for lone_collection func""" 
    return ArtObject.query.filter(ArtObject.collection_id==collection_id).first()


############################################################################################################

# #wip-hardcoded fk's <----these are audio guides
def get_sound_by_museum_id(museum_id):
    """as a patron i want to view more info about a indiviual Collection's 4-5 related sounds"""
    return RelatedSound.query.filter(RelatedSound.museum_id==museum_id).first()

# #should be replaced by CollectionSound table
# def get_sound_by_coll_id(museum_id):
#     """as a patron i want to view more info about a indiviual Collection's 4-5 related sounds"""
#     return CollectionSound.get()

#this should get sounds for musem?
#check for other magic vars in crud
#Museum.query.filter(Museum.related_sound==sound_id).first()

#have yet to query or .get the CollectionSound table fpr get_coll_sound(collection_id, related_sound_id)












##########CRUD FOR SEEDING
# works
def create_museum(name, street, city, state, zipcode, weburl):
    """create museum object 1x so seed can repeatedly"""
    return Museum(name=name, street=street, city=city, state=state, zipcode=zipcode, weburl=weburl) #removed 'collection=c1'
    #m1=model.Museum(name='Houston Museum of African American Culture', city='Houston', state='TX', country='USA') #removed 'collection=c1'

############################################################################################################
#                                                                                                          #
#                                            MUSEUM-CRUD FOR SERVER                                        #
#                                                                                                          #
############################################################################################################

#works
def get_museums():
    """read all museum data..collections that ill for loop through in jinja once i pass it into view func""" 
    return Museum.query.all()
    
#works
def get_museum_by_id(id):
    """read all museum data..collections that ill for loop through in jinja once i pass it into view func""" 
    return Museum.query.get(id)
    




















##########CRUD FOR SEEDING
#works
def create_art_object(artist, title, medium, description, era, img_path, collection_id): #DONE
    """create art object by hand"""
    return ArtObject(artist=artist, title=title, medium=medium, description=description, era=era, img_path=img_path, collection_id=collection_id) #add c3, c2

############################################################################################################
#                                                                                                          #
#                                       ART OBJECT=CRUD FOR SERVER                                         #
#                                                                                                          #
############################################################################################################

#w/o api-pre-loading
#artobj via collectionid <----hardcode server

#brooklyn_api:show images on front-end 

#w/ api-NOT DOING THIS 
# api would get new info thats not in dd, capture that data through 
# hidden form{in hidden form, allow patron to select}, send to db, create new row in art 
# object table....that would save coll id in there as an FK, and it would 
# be called artob.collection_id...


#works-hardcoded fk's
def get_art_by_id(id): #collection_id is passed in via route
    """artobj via id to show deets""" 
    return ArtObject.query.get(id)
    

def get_art():
    """read all art obj data""" 
    return ArtObject.query.all()
    

















##########CRUD FOR SEEDING
def create_related_sound(medium, sound_name, description, genre, sound_source, museum_id): #DONE
    """create related_sound object...by hand"""
    return RelatedSound(medium=medium, sound_name=sound_name, description=description, genre=genre, sound_source=sound_source, museum_id=museum_id) 

###########################################################################################################
#                                                                                                          #
#                                       RELATED SOUNDS-CRUD FOR SERVER                                     #
#                                                                                                          #
############################################################################################################

#works
def get_sounds():
    """read all sound data""" 
    return RelatedSound.query.all()
    
#works
def get_sound_by_id(id):
    """read all sound data""" 
    return RelatedSound.query.get(id)
    



























##crud.py deals with db connections, this dunder main will connect you to the database when you run crud.py interactively
if __name__ == '__main__':
    from server import app
    with app.app_context():
        connect_to_db(app)


# hard-coding FAVORTIES to patrons for testing db
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

# def get_art_object_fave(favorite):
# # def summon_art_object_fave(art_obj, patron):
#     # art_fave=ArtFave(patron_id=patron_id,art_id=art_id) #accidentally enlisted help of fk's
#     art_fave=ArtFave(favorite=favorite) #either patron and art fk's or art_fave relationship majic var 
#     #fave=ArtFave(art_obj=art_obj, patron=patron) #either patron and art fk's or art_fave relationship majic var 
#     patron.art_fave.append(art_fave)
#     return 

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
