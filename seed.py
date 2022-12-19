"""Script to seed database."""
#With an ORM, your model classes (who inherited from the Flask Model class) 
# have built-in functions for selection.

import os
#import json #use when i import museum data
from random import choice
import crud
import model
import server

os.system('dropdb muse --if-exists')
os.system(f'createdb muse')

model.connect_to_db(server.app)
model.db.create_all()

#[x]    append 4 types of faves onto patron     4
#[x]    append multiple arts onto 1 collection   1
#[x]    append multiple sounds onto 1 collection via magic var   1
#[x]    append multiple sounds onto museum                       1
#[x]    append 1 collection onto 1 museum        1

#=8 relationships, most bidirectional

#[x]    create patron, museum, art, collection and sound classes        5

#other:
#(4) faves tables are auto generated        :)
#collection sounds table is auto generated  :)

######################################################################

#create empty collection!
coll_in_db=[]
for n in range(10):
    coll_category=f'category{n}'
    name=f'nameofartwork{n}'
    description=f'description{n}'
    curator=f'curator{n}'
    era=f'era{n}'
    num_items=int(n) ##########may be invalid
    
    db_collection=crud.create_collection(coll_category, name, description, curator, era, num_items)
    coll_in_db.append(db_collection)
model.db.session.add_all(coll_in_db)


#create artobject! later feed data in via api!
#trouble connecting bc forign key
art_objects_in_db=[]
for n in range(10):
    artist=f'artistis{n}'
    title=f'titleofartwork{n}'
    medium=f'mediumis{n}'
    description=f'description{n}'
    era=f'description{n}'
    col_id=n+1 #not clean #FK
    
    db_art_object=crud.create_art_object(artist, title, medium, description, era, col_id) #db_collection[n][0]
    art_objects_in_db.append(db_art_object)
model.db.session.add_all(art_objects_in_db)


#put art into empty collection!
# mini_coll=[]
# for n in range(db_collection):
#     coll_category=f'category{n}'
#     name=f'name of artwork{n}'
#     description=f'description{n}'
#     curator=f'creator{n}'
#     era=f'era{n}'
#     num_items=f'num is {n}'
    
#     filled_collection=crud.create_collection(coll_category, name, description, curator, era, num_items)
#     model.db.session.add(db_collection)


#create museum! later feed data in csv->json
museums_in_db=[]
for n in range(10):
    name=f'nameofmuseum{n}'
    city=f'city{n}'
    state=f'state{n}'
    country=f'country{n}'

    db_museum=crud.create_museum(name, city, state, country)
    museums_in_db.append(db_museum)
model.db.session.add_all(museums_in_db)

#create related sound! later feed data in via api!
sounds_in_db=[]
for n in range(10):
    medium=f'mediumis{n}'
    sound_name=f'soundnameis{n}'
    description=f'description{n}'
    genre=f'genre{n}'
    mus_id=n+1 #FK
    
    db_related_sound=crud.create_related_sound(medium, sound_name, description, genre, mus_id)
    sounds_in_db.append(db_related_sound)
model.db.session.add_all(sounds_in_db)


#create patron!
patrons_in_db=[]
for n in range(10): #goes through each 10x for 10 patrons! #should i use enumerate? for it to be a patron speciifc parse?
    uname= f'user{n}'
    fname= f'nameis{n}'
    lname= f'lastnameis{n}'
    email= f'user{n}@test.com'
    pword= f'pwordis{n}'
    
    db_patron=crud.create_patron(uname, fname, lname, email, pword)
    patrons_in_db.append(db_patron)
    model.db.session.add_all(patrons_in_db)

    #will produce over 200 entries for 10 patrons, 20 faves per patron, 5 faves in 4 categories
    #create patron art faves
    # for _ in range(5):
    #     art_fave=crud.summon_art_object_fave(db_patron.p_id, db_art_object.id)
    # # # Use choice to get a random art object from art_obj_in_db and random patron
    #     # random_artobj=choice(art_objects_in_db)
    #     # db_artfave=crud.summon_art_object_fave(random_artobj, db_patron)
    #     model.db.session.add(art_fave) #should be adding this linkup to the art fave table

        # model.db.session.add(db_artfave)
        # linkup=db_patron.append(db_artfave) #i only want it to do this for the patron its on in the loop
        # model.db.session.add(linkup) #should be adding this linkup to the art fave table

    # for _ in range(5):
    # # # Use choice to get a random art object from art_obj_in_db and random patron
    #     random_artobj=choice(art_objects_in_db)
    #     patron=db_patron
    #     rel=crud.summon_art_object_fave(db_patron) #a lot going on
    #     model.db.session.add(rel) #needed?
    #     art_fave=db_patron.append(random_artobj) #i only want it to do this for the patron its on in the loop
    #     model.db.session.add(art_fave) #should be adding this linkup to the art fave table


    # for _ in range(5): #test if this produces 5 faves
    #     random_artobj=choice(art_objects_in_db) #list of art objects?
    #     random_patron=choice(patrons_in_db)
    #     db_artfave=crud.summon_art_object_fave(art_fave=db_art_object) #key iterating over id's
    #     #db_artfave=crud.summon_art_object_fave(art_fave=db_art_object)        # db_artfave=crud.summon_art_object_fave(db_patron.p_id, db_art_object.id)  
    #     #(art_fave=db_art_obj['id'])
    #     #(art_fave=db_art_obj['id'][i])
    #     model.db.session.add(db_artfave)
    #     #making a list of favorites doesnt make sense bc faves are unique to patrons, unlike museums, collections, sounds
    #     #one fave or multiple?
    #     # db_art_fave=model.ArtFave(art_fave=art_objects_in_db[i]) #i think this goes in crud
    #     linkup=random_patron.append(db_artfave)
    #     model.db.session.add(linkup) #add this binding to db!

    # create patron museum faves
    # for _ in range(5):
    #     random_museum=choice(museums_in_db) #list of museums?
    #     db_musfave=crud.summon_museum_fave(db_patron.p_id,  db_museum.id)
    #     model.db.session.add(db_collfave)

    # create patron collection faves
    # for _ in range(5):
    #     random_coll=choice(coll_in_db) #list of collections?
    #     db_collfave=crud.summon_collection_fave(db_patron.p_id, db_collection.id)
    #     model.db.session.add(db_collfave)
    
    # create patron sound faves
    # for _ in range(5):
    #     #multiple favorites here
    #     random_sound=choice(sounds_in_db) #list of sounds?
    #     db_soundfave=crud.summon_sound_fave(db_patron.p_id, db_related_sound.id)
    #     model.db.session.add(db_soundfave)




    #DONT USE----
    #pattern match assoc table(Ratings)class from movie ratings
        # for x in range(10): ####i missed this
        #     random_movie=choice(movies_in_db)
        #     score=randint(1, 5)
        #     db_rating=crud.create_rating(db_user, random_movie, score) ########
        #     model.db.session.add(db_rating)

###################################################################
# test_instances=[patrons_in_db, art_objects_in_db, coll_in_db, sounds_in_db, museums_in_db]
# model.db.session.add_all(test_instances)

model.db.session.commit() #this commit is even for the gluing favorites to each patron





# # patrons....patrons will be fake
# patron=model.Patron(uname='e', fname='ee', lname='p', email='test@test.com', pword='1234')
# patron1=model.Patron(uname='t', fname='er', lname='o', email='test1@test.com', pword='104')
# patron2=model.Patron(uname='ty', fname='eri', lname='oe', email='test2@test.com', pword='109')
# patron3=model.Patron(uname='tyk', fname='erik', lname='oeg', email='test3@test.com', pword='1090')

# c1 = model.Collection(coll_category="paint",name="paintings",description="words go here",curator="someone")
# c2 = model.Collection(coll_category="drawing",name="paintings by e",description="words go here too",curator="someone else")
# c3 = model.Collection(coll_category="sculpture",name="paintings by r",description="words go here as well",curator="monet")
# c4 = model.Collection(coll_category="print",name="rawr xd",description="words....", curator="picasso")

# #museums...real data will come from csv file i turn into json and feed into db
# #on the data side, figure out how to add a coloumn that reps the colections and figure out how to sort diff 
# #collections into museums! there will be musuem collections and curated virtual collections not found irl

# m1=model.Museum(name='Houston Museum of African American Culture', city='Houston', state='TX', country='USA') #removed 'collection=c1'
# m2=model.Museum(name='Museum of Fine Arts', city='Houston', state='TX', country='USA')
# m3=model.Museum(name='Chicago Contemporary', city='Chicago', state='IL', country='USA')  #add c3, c2
# m4=model.Museum(name='Kinder and Nacny Rich Contemporary Arts Museum', city='Houston', state='TX', country='USA')  #add c3, c2
# m5=model.Museum(name='MoMA', city='NYC', state='NY', country='USA') #add c3, c2

# #related sounds-cloudinary API-filled w/ audio museum gives me or spotify embed, fake data to test first
# sound1=model.RelatedSound(medium="podcast", sound_name="7th chapel",  description="gold foil walls", museum=m1) #add m3, m2
# sound2=model.RelatedSound(medium="song", sound_name="Luka Doncic speaks on...",  description="yellow tinted scene", museum=m1) #add m3, m2
# sound3=model.RelatedSound(medium="playlist", sound_name="Words from the curator",  description="Spaghetti", museum=m1) #add m3, m2
# sound4=model.RelatedSound(medium="commentary", sound_name="At Last",  description="baloons", genre="n/a", museum=m1) #add m3, m2

# #art objects...having trouble-API, fake data to test first
# a1=model.ArtObject(artist="M Angelo", title="7th chapel", medium="paint", description="gold foil walls", collection=c1) #add c3, c2
# a2=model.ArtObject(artist="Calder", title="Homerun", medium="sculpture", description="oil on cieling", collection=c2) #add c3, c2
# a3=model.ArtObject(artist="Hurston", title="Home Sweet Home", medium="print", description="modest", collection=c1) #add c3, c2
# a4=model.ArtObject(artist="Ligon", title="Love is", medium="paint", description="beautiful", collection=c2) #add c3, c2
# a5=model.ArtObject(artist="Basquiat", title="Untitled", medium="paint", description="wow", collection=c3) #add c3, c2

# #(4) favorites tables' business:
# #adding faves to different patrons
# #my 4 faves mapping tables automatically generate records/rows from appending instances of art, museum, rs, and collection to patrons!

# #leave these alone as far as the instance list is 
# # concerned...bc these are not db.session.add
# # ONLY need the db.session.commit() on these additions
# patron.collection_fave.append(c1) 

# i want to glue a fave to each patron syntacitically. by id FK
# create relational instance objects via magic variables in a non-function way?

# patron.collection_fave.append(c2) 
# patron1.collection_fave.append(c3) 
# patron2.collection_fave.append(c4)  
# patron3.collection_fave.append(c4)

# patron.art_fave.append(a1) 
# patron1.art_fave.append(a2)
# patron2.art_fave.append(a3)
# patron2.art_fave.append(a4)
# patron3.art_fave.append(a4)

# patron.related_sound_fave.append(sound1) 
# patron1.related_sound_fave.append(sound2)
# patron1.related_sound_fave.append(sound3)
# patron2.related_sound_fave.append(sound3)
# patron3.related_sound_fave.append(sound4)

# patron.museum_fave.append(m1)
# patron1.museum_fave.append(m2)
# patron2.museum_fave.append(m3)
# patron3.museum_fave.append(m3)
# patron3.museum_fave.append(m4)

# #collections and rs business:
# #add multiple rs onto 1 collection via magic var
# c1.related_sound.append(sound1)   #multiple rs id's show up on 1 coll in collections_sounds table!!!
# c1.related_sound.append(sound2)  
# c2.related_sound.append(sound1) 
# c2.related_sound.append(sound4) 
# c3.related_sound.append(sound3)  
# c4.related_sound.append(sound4)  

# #add multiple rs onto museum, 1 museum, multiple sounds  
# m1.related_sound.append(sound1)  #solved: the museum id shows up on multiple art sounds !!!
# m1.related_sound.append(sound2)    
# m2.related_sound.append(sound1)  
# m3.related_sound.append(sound1)   
# m4.related_sound.append(sound1)                  

# #art objects business:
# #how can i see what art objects are in collection, or do i view art object and its a coloumn of the collectionit belongs to ?
# c1.art_object.append(a1) #solved: the collection id shows up on multiple art objects !!!
# c1.art_object.append(a2)
# c2.art_object.append(a3)
# c3.art_object.append(a2)
# c4.art_object.append(a1)
# c4.art_object.append(a3)


















# ####################################
# #2.0
# #museum's business:
# #add 1 collection onto 1 museum        
# # c1.museum.append(m1) #1 for 1! might need an if statement to prevent multiples
# # c2.museum.append(m2) #collection id shows up on museum table..i need the 
# # c3.museum.append(m3) #refresh last to see changes, uselist
# # c4.museum.append(m4)


