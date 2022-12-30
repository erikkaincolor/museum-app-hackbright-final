"""Script to seed database."""

import os
import json 
#from random import choice
import crud
import model
import server

os.system('dropdb muse --if-exists')
os.system(f'createdb muse')

model.connect_to_db(server.app)
model.db.create_all()

#create empty collection!
c1 = crud.create_collection("women","Awesome Black Radical Women, 1965–85","Women of color found themselves collaborating with and occasionally opposing the predominantly white, middle-class women who were primarily in charge of setting the tone, goals, and strategies for the battle for gender parity in the US during the second wave of feminism in the 1970s.","E. Polk", "Spiral, Black Arts Movement")
c2 = crud.create_collection("photography","Darkroom: Black and White Photos See the Light of Day","Photos of Black people from all over the diaspora, up close and in black and white.","E. Polk", "Contemporary")
c3 = crud.create_collection("mixed media","Contemporaries in Color","This collection displays African-Americna Art in the form of paint, mixed media and depicts people in natural state.","E. Polk", "THE BLACK ARTS MOVEMENT")
c4 = crud.create_collection("screenprint","Dip, Roll, and Print: Cleveland Bellow, American, 1946-2009","Cleveland Bellow portrayed Black musicians and activists in his graphic prints, as well as regular people like the young child in Untitled who is holding his hands behind his head. This piece subsequently became a billboard in Oakland, California as part of the national trend of public Black art.", "E. Polk", "Black Arts Movement")
collections=[c1, c2, c3, c4]
model.db.session.add_all(collections)
model.db.session.commit()  

#create artobject! later feed data in via api!
# a1=crud.create_art_object("Barbara Jones-Hogu", "Nation Time", "print", "Barbara Jones-Hogu (American, 1938-2017). Nation Time, ca. 1970. Color screenprint, sheet: 22 1/2 x 30 in. (57.2 x 76.2 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.25. artist or artist's estate (Photo: Brooklyn Museum, 2012.80.25_PS4.jpg) ","Black Arts Movement", collection_id=c1.id) #add c3, c2
# a2=crud.create_art_object("Dindga McCannon", "Empress Akweke", "paint", " Dindga McCannon (American, born 1947). Empress Akweke, 1975. Acrylic on canvas, 35 7/8 × 31 15/16 × 13/16 in. (91.1 × 81.1 × 2.1 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.31. artist or artist's estate (Photo: Brooklyn Museum, 2012.80.31_PS9.jpg) ","Black Arts Movement", collection_id=c1.id) #add c3, c2
# a3=crud.create_art_object("Betye Saar", "Liberation of Aunt Jemima: Cocktail", "glass, paper, textile, metal", "Betye Saar (American, born 1926). Liberation of Aunt Jemima: Cocktail, 1973. Glass, paper, textile, metal, Overall: 12 1/2 × 5 3/4 in. (31.8 × 14.6 cm). Brooklyn Museum, Purchased with funds given by Elizabeth A. Sackler, gift of the Contemporary Art Committee, and William K. Jacobs, Jr. Fund, 2017.17. © artist or artist's estate (Photo: , 2017.17_front_PS11.jpg) ","Black Arts Movement", collection_id=c1.id) #add c3, c2

# a4=crud.create_art_object("Tony Gleaton", "Black Girl, White Flower, Belize, Central America", "photograph", " Tony Gleaton (American, 1948-2015). Black Girl, White Flower, Belize, Central America, 1992. Gelatin silver photograph, image: 15 3/4 x 14 3/4 in. (40 x 37.5 cm). Brooklyn Museum, Gift of Helen Griffith in memory of Seymour Griffith, 1997.134. © artist or artist's estate (Photo: Brooklyn Museum, 1997.134_transp5713.jpg) ","Contemporary Art Movement", collection_id=c2.id) #add c3, c2
# a5=crud.create_art_object("Tony Gleaton", "Un Hija de Jesus, Guatemala, Latin America, (Daughter of Jesus)", "photograph", " Tony Gleaton (American, 1948-2015). Un Hija de Jesus, Guatemala, Latin America, (Daughter of Jesus), 1992. Gelatin silver photograph, image: 15 3/4 x 14 3/4 in. (40.0 x 37.5 cm). Brooklyn Museum, Purchased with funds given by Karen B. Cohen and Jan Staller, 1997.50. artist or artist's estate (Photo: Brooklyn Museum, 1997.50_bw.jpg)", "Contemporary Art Movement",collection_id=c2.id) #add c3, c2
# a6=crud.create_art_object("Sarah A. Friedman", "Untitled, Brooklyn, New York", "photograph", "Sarah A. Friedman (American). Untitled, Brooklyn, New York. Chromogenic photograph, Image: 19 1/2 x 15 1/2 in. (49.5 x 39.4 cm). Brooklyn Museum, Gift of the artist, 2001.110.2. Creative Commons-BY (Photo: Brooklyn Museum, 2001.110.2_bw.jpg) ","Contemporary Art Movement", collection_id=c2.id) #add c3, c2

# a7=crud.create_art_object("Nelson Stevens", "Uhuru", "print", "Nelson Stevens (American, born 1938). Uhuru, 1971. Screenprint on paper, Sheet: 40 x 30 in. (101.6 x 76.2 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.41. artist or artist's estate (Photo: Brooklyn Museum, 2012.80.41_PS6.jpg) ","Black Arts Movement",collection_id=c3.id) #add c3, c2
# a8=crud.create_art_object("Marie Johnson Calloway", "The Winner", "print", "Marie Johnson Calloway (American, 1920 - 2018). The Winner, 1971. Mixed media (acrylic, fabric) on wood, 60 x 30 in. (152.4 x 76.2 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.19. artist or artist's estate (Photo: Brooklyn Museum, CUR.2012.80.19.jpg) ","Black Arts Movement", collection_id=c3.id) #add c3, c2
# a9=crud.create_art_object("Glenn Ligon", "[Untitled] (Crowd/The Fire Next Time)", "print", "The accumulation of crystals suggests the mass of participants in this historic event as viewed from above, while the juxtaposition of Baldwin’s words with the image of the march—separated by more than three decades—reminds us of the still-ongoing dialogue about race in America. Screenprint with coal crystals on paper, image: 12 × 18 1/8 in. (30.5 × 46 cm). Brooklyn Museum, Alfred T. White Fund, 2000.56. artist or artist's estate (Photo: Brooklyn Museum, 2000.56_transp5856.jpg)", "Contemporary Art Movement",collection_id=c3.id) #add c3, c2

# a10=crud.create_art_object("Cleveland Bellow", "George Jackson", "print", "Cleveland Bellow (American, 1946-2009). George Jackson, 1970. Screenprint on colored paper, Sheet: 23 1/2 x 17 1/2 in. (59.7 x 44.5 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.8. © artist or artist's estate (Photo: Brooklyn Museum, 2012.80.8_PS4.jpg)", "Black Arts Movement",collection_id=c4.id) #add c3, c2
# a11=crud.create_art_object("Cleveland Bellow", "Untitled", "print", "Cleveland Bellow (American, 1946-2009). Untitled, 1968. Screenprint on paper, sheet: 19 1/2 x 15 1/4 in. (49.5 x 38.7 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.6. © artist or artist's estate (Photo: Brooklyn Museum, 2012.80.6_PS4.jpg)", "Black Arts Movement",collection_id=c4.id) #add c3, c2
# a12=crud.create_art_object("Cleveland Bellow", "Duke", "print", "Cleveland Bellow (American, 1946-2009). Duke, 1968. Unique screenprint on two sheets of acrylic, Sheet: 28 x 22 in. (71.1 x 55.9 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.7. artist or artist's estate (Photo: Brooklyn Museum, CUR.2012.80.7.jpg) ", "Black Arts Movement",collection_id=c4.id) #add c3, c2
# art_objects=[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
# model.db.session.add_all(art_objects)
# model.db.session.commit() 

#test last
#put art into empty collection!
# mini_coll=[]
# for n in range(db_collection):
#     f'category{n}'
#     name=f'name of artwork{n}'
#     description=f'description{n}'
#     f'creator{n}'
#     f'era{n}'
#     num_items=f'num is {n}'
    
#     filled_crud.create_collection(coll_category, name, description, curator, era, num_items)
#     model.db.session.add(db_collection)

#create museum! later feed data in csv->json

with open('data/aa_museums.json') as f: #Now, museums will be a list of dictionaries
    aa_museum_data = json.loads(f.read())

museums_in_db=[]
for museum in aa_museum_data:
    name=museum['NAME']
    street=museum['STREET']
    city=museum['CITY']
    state=museum['STATE']
    zipcode=museum['ZIPCODE']
    weburl=museum['WEBURL']
    # collection_id=n+1

    db_museum=crud.create_museum(name, street, city, state, zipcode, weburl)
    # db_museum=crud.create_museum(name, street, city, state, zipcode, url, collection_id)
    museums_in_db.append(db_museum)
model.db.session.add_all(museums_in_db)
model.db.session.commit()  

#worked when i needed samples
# mus1=crud.create_museum('BUFFALO SOLDIERS NATIONAL MUSEUM', '3816 CAROLINE ST', 'Houston', 'TX', '77004', 'HTTP://BUFFALOSOLDIERMUSEUM.COM/', collection_id=c1.id) #NOT collection_id=c1
# mus2=crud.create_museum('HOUSTON MUSEUM OF AFRICAN AMERICAN CULTURE', '4807 CAROLINE ST' 'Houston', 'TX', '77004', 'HTTPS://HMAAC.ORG/', collection_id=c2.id )
# mus3=crud.create_museum('CALABOOSE AFRICAN AMERICAN HISTORY MUSEUM', '200 W MARTIN LUTHER KING DR', 'San Marcos', 'TX', '78666', 'HTTP://SANMARCOSARTS.COM', collection_id=c3.id)
# mus4=crud.create_museum('LUCY CRAFT LANEY MUSEUM OF BLACK HISTORY','1116 PHILLIPS ST', 'Augusta', 'GA','30901' 'HTTPS://LUCYCRAFTLANEYMUSEUM.COM/', collection_id=c4.id)
# museums=[mus1, mus2, mus3, mus4]
# model.db.session.add_all(museums)
# model.db.session.commit()  


#create related sound! later feed data in via api!
# sounds_in_db=[]
# for n in range(10):
#     medium=f'mediumis{n}'
#     sound_name=f'soundnameis{n}'
#     description=f'description{n}'
#     genre=f'genre{n}'
#     museum_id=n+1 #FK <------
    
#     db_related_sound=crud.create_related_sound(medium, sound_name, description, genre, museum_id)
#     sounds_in_db.append(db_related_sound)
# model.db.session.add_all(sounds_in_db)



#create patron!
patrons_in_db=[]
# for n in range(10): #goes through each 10x for 10 patrons! #should i use enumerate? for it to be a patron speciifc parse?
#     uname= f'user{n}'
#     fname= f'nameis{n}'
#     lname= f'lastnameis{n}'
#     email= f'user{n}@test.com'
#     pword= f'pwordis{n}'
    
#     db_patron=crud.create_patron(uname, fname, lname, email, pword)
#     patrons_in_db.append(db_patron)
#     model.db.session.add_all(patrons_in_db)

p1=crud.create_patron("erikkaincolor", "Erikka", "Polk", "erikkaincolor@gmail.com", "1234")
p2=crud.create_patron("artistsmus3", "Glenn", "Ligon", "glennlig0n@gmail.com", "4321")
p3=crud.create_patron("solangel", "Solange", "Knowles", "solange@gmail.com", "abcd")

patrons=[p1, p2, p3]
model.db.session.add_all(patrons)
model.db.session.commit()  








    #test last----most difficulty
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



#related sounds-cloudinary API-filled w/ audio museum gives me or spotify embed, fake data to test first
# sound1=model.RelatedSound("podcast", sound_name="7th chapel",  "gold foil walls", museum=m1) #add m3, m2
# sound2=model.RelatedSound("song", sound_name="Luka Doncic speaks on...",  "yellow tinted scene", museum=m1) #add m3, m2
# sound3=model.RelatedSound("playlist", sound_name="Words from the curator",  "Spaghetti", museum=m1) #add m3, m2
# sound4=model.RelatedSound("commentary", sound_name="At Last",  "baloons", genre="n/a", museum=m1) #add m3, m2

# #(4) favorites tables' business:
# #adding faves to different patrons
# #my 4 faves mapping tables automatically generate records/rows from appending instances of art, museum, rs, and collection to patrons!

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
