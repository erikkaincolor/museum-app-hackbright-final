"""Script to seed database."""
#With an ORM, your model classes (who inherited from the Flask Model class) 
# have built-in functions for selection.

import os

os.system(f'dropdb muse --if-exists')
os.system(f'createdb muse')

import model
import server

model.connect_to_db(server.app)

# Updates the database schema
model.db.create_all()

# patrons....patrons will be fake
patron=model.Patron(uname='e', fname='ee', lname='p', email='test@test.com', pword='1234')
patron1=model.Patron(uname='t', fname='er', lname='o', email='test1@test.com', pword='104')
patron2=model.Patron(uname='ty', fname='eri', lname='oe', email='test2@test.com', pword='109')
patron3=model.Patron(uname='tyk', fname='erik', lname='oeg', email='test3@test.com', pword='1090')

c1 = model.Collection(coll_category="paint",name="paintings",description="words go here",curator="someone")
c2 = model.Collection(coll_category="drawing",name="paintings by e",description="words go here too",curator="someone else")
c3 = model.Collection(coll_category="sculpture",name="paintings by r",description="words go here as well",curator="monet")
c4 = model.Collection(coll_category="print",name="rawr xd",description="words....", curator="picasso")

#museums...real data will come from csv file i turn into json and feed into db
#on the data side, figure out how to add a coloumn that reps the colections and figure out how to sort diff 
#collections into museums! there will be musuem collections and curated virtual collections not found irl

m1=model.Museum(name='Houston Museum of African American Culture', city='Houston', state='TX', country='USA') #removed 'collection=c1'
m2=model.Museum(name='Museum of Fine Arts', city='Houston', state='TX', country='USA')
m3=model.Museum(name='Chicago Contemporary', city='Chicago', state='IL', country='USA')  #add c3, c2
m4=model.Museum(name='Kinder and Nacny Rich Contemporary Arts Museum', city='Houston', state='TX', country='USA')  #add c3, c2
m5=model.Museum(name='MoMA', city='NYC', state='NY', country='USA') #add c3, c2

#related sounds-cloudinary API-filled w/ audio museum gives me or spotify embed, fake data to test first
sound1=model.RelatedSound(medium="podcast", sound_name="7th chapel",  description="gold foil walls", museum=m1) #add m3, m2
sound2=model.RelatedSound(medium="song", sound_name="Luka Doncic speaks on...",  description="yellow tinted scene", museum=m1) #add m3, m2
sound3=model.RelatedSound(medium="playlist", sound_name="Words from the curator",  description="Spaghetti", museum=m1) #add m3, m2
sound4=model.RelatedSound(medium="commentary", sound_name="At Last",  description="baloons", genre="n/a", museum=m1) #add m3, m2

#art objects...having trouble-API, fake data to test first
a1=model.ArtObject(artist="M Angelo", title="7th chapel", medium="paint", description="gold foil walls", collection=c1) #add c3, c2
a2=model.ArtObject(artist="Calder", title="Homerun", medium="sculpture", description="oil on cieling", collection=c2) #add c3, c2
a3=model.ArtObject(artist="Hurston", title="Home Sweet Home", medium="print", description="modest", collection=c1) #add c3, c2
a4=model.ArtObject(artist="Ligon", title="Love is", medium="paint", description="beautiful", collection=c2) #add c3, c2
a5=model.ArtObject(artist="Basquiat", title="Untitled", medium="paint", description="wow", collection=c3) #add c3, c2

#(4) favorites tables' business:
#adding faves to different patrons
#my 4 faves mapping tables automatically generate records/rows from appending instances of art, museum, rs, and collection to patrons!

#leave these alone as far as the instance list is 
# concerned...bc these are not db.session.add
# ONLY need the db.session.commit() on these additions
patron.collection_fave.append(c1) 
patron.collection_fave.append(c2) 
patron1.collection_fave.append(c3) 
patron2.collection_fave.append(c4)  
patron3.collection_fave.append(c4)

patron.art_fave.append(a1) 
patron1.art_fave.append(a2)
patron2.art_fave.append(a3)
patron2.art_fave.append(a4)
patron3.art_fave.append(a4)

patron.related_sound_fave.append(sound1) 
patron1.related_sound_fave.append(sound2)
patron1.related_sound_fave.append(sound3)
patron2.related_sound_fave.append(sound3)
patron3.related_sound_fave.append(sound4)

patron.museum_fave.append(m1)
patron1.museum_fave.append(m2)
patron2.museum_fave.append(m3)
patron3.museum_fave.append(m3)
patron3.museum_fave.append(m4)

#collections and rs business:
#add multiple rs onto 1 collection via magic var
c1.related_sound.append(sound1)   #multiple rs id's show up on 1 coll in collections_sounds table!!!
c1.related_sound.append(sound2)  
c2.related_sound.append(sound1) 
c2.related_sound.append(sound4) 
c3.related_sound.append(sound3)  
c4.related_sound.append(sound4)  

#museum's business:
#add 1 collection onto 1 museum        
# c1.museum.append(m1) #1 for 1! might need an if statement to prevent multiples
# c2.museum.append(m2) #collection id shows up on museum table..i need the 
# c3.museum.append(m3) #refresh last to see changes, uselist
# c4.museum.append(m4)

#add multiple rs onto museum, 1 museum, multiple sounds  
m1.related_sound.append(sound1)  #solved: the museum id shows up on multiple art sounds !!!
m1.related_sound.append(sound2)    
m2.related_sound.append(sound1)  
m3.related_sound.append(sound1)   
m4.related_sound.append(sound1)                  

#art objects business:
#how can i see what art objects are in collection, or do i view art object and its a coloumn of the collectionit belongs to ?
c1.art_object.append(a1) #solved: the collection id shows up on multiple art objects !!!
c1.art_object.append(a2)
c2.art_object.append(a3)
c3.art_object.append(a2)
c4.art_object.append(a1)
c4.art_object.append(a3)




















###################################################################
test_instances=[patron, patron1, patron2, patron3, c1, c2, c3, c4, a1, a2, a3, a4, m1, m2, m3, m4]

model.db.session.add_all(test_instances) #<----similar to db.session.add()
#^put all of the instances in list and pass th elist
model.db.session.commit()





#[x]   append 4 types of faves onto patron     4
#[x]    append multiple arts onto 1 collection   1
#[x]    append multiple rs onto 1 collection via magic var   1
#[x]    append multiple rs onto museum                       1
#[x]    append 1 collection onto 1 museum        1

#=8 connections, most bidirectional bc of relationship 

#other:
#(4) faves tables are auto generated        :)
#collection sounds table is auto generated  :)