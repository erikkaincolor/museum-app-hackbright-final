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
    patron=Patron(uname=uname, fname=fname, lname=lname, email=email, pword=pword)
    return patron
    #patron=model.Patron(uname='e', fname='ee', lname='p', email='test@test.com', pword='1234')


############################################################################################################
#                                                                                                          #
#                                       PATRON FAVES-CRUD FOR SERVER                                       #
#                                                                                                          #
############################################################################################################

#works
def create_museum_fave(patron_id, museum_id): #fk's to museum faves
    """create a museum favorite"""
    return MuseumFave(patron_id=patron_id, museum_id=museum_id)

# works
def get_m_fave_by_id(id):
    """for deleting from db and showing up on patrons profile"""
    return MuseumFave.query.get(id)

#works
def create_collection_fave(patron_id, collection_id): #fk's to collection faves
    """create a museum favorite..seed db side and server side"""
    return CollectionFave(patron_id=patron_id, collection_id=collection_id)

#works
def get_c_fave_by_id(id):
    """for deleting from db and showing up on patrons profile"""
    return CollectionFave.query.get(id)

#------------------------------

#WIP test when art renders
def create_art_fave(patron_id, art_id): #fk's to collection faves
    """create a museum favorite..seed db side and server side"""
    return ArtFave(patron_id=patron_id, art_id=art_id)

#WIP
def get_a_fave_by_id(id):
    """for deleting from db and showing up on patrons profile"""
    return ArtFave.query.get(id)


#WIP-test when page is setup!
def create_sound_fave(patron_id, related_sound_id): #fk's to collection faves
    """create a museum favorite..seed db side and server side"""
    return RelatedSoundFave(patron_id=patron_id, related_sound_id=related_sound_id)

#WIP
def get_s_fave_by_id(id):
    """for deleting from db and showing up on patrons profile"""
    return RelatedSoundFave.query.get(id)


# <button value="{{collection.id}}">Add to favorites </button> <br><br>
#IS THIS WHERE I USE RELATIONSHIP??


# -update MuseumFave /update-favoite, via ajax later
# -add faves to patron profile /patron-profile/{patron.id}/favorite
# -this form and button will show up on museum details, collection details and art object details

#havent shown proof they work for server:
# def update_museum_fave(patron_id):
#     #if museumfave exists for this patron already
#     #delete all except one
#     #if patron id in db matches the given one:
#     multiples=[]
#     if MuseumFave.query.filter(MuseumFave.patron_id == patron_id).one() is False: #if theres more than one
#         multiples[1:].append(patron_id) #skip first occurance
#         return multiples










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
    patron=Patron(uname=uname, fname=fname, lname=lname, email=email, pword=pword)
    return patron























##########CRUD FOR SEEDING
#works
def create_collection(coll_category, name, description, curator, era):
    """create collection object 1x so seed can repeatedly"""
    collection= Collection(coll_category=coll_category,name=name,description=description,curator=curator, era=era)
    return collection

#works
def create_collection_sound(collection_id, related_sound_id): #fk's to collection faves
    """create a collection sound..seed db side and server side"""
    collection_sound=CollectionSound(collection_id=collection_id, related_sound_id=related_sound_id)
    return collection_sound

############################################################################################################
#                                                                                                          #
#                                   COLLECTIONS-CRUD FOR SERVER                                            #
#                                                                                                          #
############################################################################################################

#works
def get_collections(): 
    """read all collection data..collections that ill for loop through in jinja once i pass it into view func""" 
    return Collection.query.all()

#works
def get_collection_id(id): #DONE
    """read all collection data..collections that ill for loop through in jinja once i pass it into view func""" 
    return Collection.query.get(id)























##########CRUD FOR SEEDING

# works
def create_museum(name, street, city, state, zipcode, weburl):
    """create museum object 1x so seed can repeatedly"""
    museum=Museum(name=name, street=street, city=city, state=state, zipcode=zipcode, weburl=weburl) #removed 'collection=c1'
    return museum
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
    art_obj=ArtObject(artist=artist, title=title, medium=medium, description=description, era=era, img_path=img_path, collection_id=collection_id) #add c3, c2
    return art_obj

############################################################################################################
#                                                                                                          #
#                                       ART OBJECT=CRUD FOR SERVER                                         #
#                                                                                                          #
############################################################################################################

#WIP
def get_art_by_id(id):
    """get ONE art obj by id""" 
    return ArtObject.query.get(id)

#WIP/ create art object on collection deets page
# def get_art_by_coll_id(collection_id): #collection_id is passed in via route
#     """artobj via collectionid to show all """ 
#     return ArtObject.query.filter(ArtObject.collection_id==collection_id).first()

#works-delete later, for
# def patron_uname_lookup(uname): #DONE #in order to call,  id have to know uname
#     """get patron by uname"""
#     return Patron.query.filter(Patron.uname == uname).first()

#WIP
# def get_art_by_coll_id(collection_id): #collection_id is passed in via route
#     """multiple artobjs via collectionid to show all """ 
#     return ArtObject(collection_id=collection_id)





#w/o api-pre-loading
#artobj via collectionid <----hardcode server

#brooklyn_api:show images on front-end 

#w/ api-NOT DOING THIS 
# api would get new info thats not in dd, capture that data through 
# hidden form{in hidden form, allow patron to select}, send to db, create new row in art 
# object table....that would save coll id in there as an FK, and it would 
# be called artob.collection_id...






















##########CRUD FOR SEEDING
def create_related_sound(medium, sound_name, description, genre, museum_id): #DONE
    """create related_sound object..by hand"""
    related_sound=RelatedSound(medium=medium, sound_name=sound_name, description=description, genre=genre, museum_id=museum_id) #museum_id may need to be hardcoded, 1, 2, 3, 4
    return related_sound

# CONNECT sound to collection-#USE FKs
#will show up on collection deets route and sound deets route

#*********************************
# FUNC STORED UNDER COLLECTION   *
#*********************************

# # CONNECT sound to museum -similar to faves assoc tables + their crud funcs
#will show up on museum deets route and sound deets route

# def marry_museum_rs():
#     """relationship object creation"""
#     m1.related_sound.append(sound2)    
#     return 
#     m1.related_sound.append(sound2)    
#     c1.related_sound.append(sound2)  

############################################################################################################
#                                                                                                          #
#                                       RELATED SOUNDS-CRUD FOR SERVER                                     #
#                                                                                                          #
############################################################################################################

# def get_related_sounds(): #DONE
#   """read all sound data..collections that ill for loop through in jinja once i pass it into view func""" 
#   return RelatedSound.query.all()


# def details_related_sounds(medium, sound_name, description, museum):
#   QUERY-#   """as a patron i want to view more info about a indiviual Collection's 4-5 related sounds"""
#   sounds_list=RelatedSound.query.all()
#   sound=RelatedSound(medium, sound_name, description, museum) #add m3, m2




























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
