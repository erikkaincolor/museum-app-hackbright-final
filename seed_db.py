"""Script to seed database."""

import os
import json 
import crud
import data.model as model
import server

os.system('dropdb muse --if-exists')
os.system(f'createdb muse')

model.connect_to_db(server.app)
model.db.create_all()

# 1/5/23:
        # SEED DB!
# check that sounds saved successfully   -  WORKS                                 
# check that art saved successfully         -  WORKS  
# # check that art saved to collections successfully via FK  -  WORKS  
        # UNCOMMENT ASSOC OBJS
        # THEN run again!
# check that sounds saved to collections successfully via crud func 
        # UNCOMMENT ASSOC OBJS
        # THEN run again!
# check that sounds saved to museums successfully via fk    

############################################################################################################
#                                                                                                          #
#   COLLECTIONS                                                                                            #
#                                                                                                          #
############################################################################################################

#create empty collections, these are created by hand 
c1 = crud.create_collection("print","Florida m(e)n compositional","Internet users typically submit links to news stories and articles about unusual or strange crimes and other events occurring in Florida, with stories' headlines often beginning with 'Florida Man...' followed by the main event of the story. These photos and collages embody Alexander Lawrence’s and Jared Carr’s lived experiences via various photo, capture and display methods.","Kara Walker", "Contemporary")
c2 = crud.create_collection("mixed","From (?) Philly w/ Love, 2021-22","A Texas native and now a Philly transplant, Tafari has constantly enamored audiences, college campuses, libraries and local communities with his colorful stream of consciousness and ability to create new worlds and frameworks in Black spaces and time warps. There’s audio, there’s culturally investigative zines, there’s even a Hotep Registration Form for self identification and literacy testing. Tafari Diop Robertson is our head curator's close friend and digitally loaned these pieces for your viewing. ","E. Polk", "Contemporary")
c3 = crud.create_collection("mixed media","Contemporaries in Color","This collection displays African-Americna Art in the form of paint, mixed media and depicts people in natural state.","E. Polk", "THE BLACK ARTS MOVEMENT")
c4 = crud.create_collection("screenprint","Dip, Roll, and Print: Cleveland Bellow, American, 1946-2009","Cleveland Bellow portrayed Black musicians and activists in his graphic prints, as well as regular people like the young child in Untitled who is holding his hands behind his head. This piece subsequently became a billboard in Oakland, California as part of the national trend of public Black art.", "E. Polk", "Black Arts Movement")
collections=[c1, c2, c3, c4]
model.db.session.add_all(collections)
model.db.session.commit()  

############################################################################################################
#                                                                                                          #
#   ART OBJECTS                                                                                            #
#                                                                                                          #
############################################################################################################

#created 1/5/23
#create artobjects-later feed data in via Cloudinary API
#update images so copyrighted ones arent used! about 4/12 of em
#collection is hardcoded via FK at end

a1=crud.create_art_object("Alexandeur Lawrence", "Eyes (2021)", "Mixed media", "A collage of digital paintings focusing on the emotions of the eyes. American, (b. 1996).","Contemporary Art Movement", "/static/img/the-collection/c1/a_1.jpeg", 1) #add c3, c2
a2=crud.create_art_object("Alexandeur Lawrence", "Screaming down 54 (2021)", "Mixed media", "'It's the end of something somewhere' Acrylic paint coats the top of a photographic print of a self-portrait. Obscuring most of the photograph except for the artists eyes. American, (b. 1996). ", "Contemporary","static/img/the-collection/c1/a_2.JPG", 1) #add c3, c2
a3=crud.create_art_object("Jared Carr", "'Untitled #77' (2019)", "Film", "Film photograph. American, (b.1997).","Contemporary", "/static/img/the-collection/c1/j_1.jpg",1) #add c3, c2 #removed collection_id=c2.id
a13=crud.create_art_object("Jared Carr", "Krystal's Foresight (2021)", "Film", "A shot of Krystal, Jared's older sister as she looks out the window. American, (b. 1997). Film photograph.","Contemporary", "/static/img/the-collection/c1/j_2.jpg",1) #add c3, c2 #removed collection_id=c2.id

a4=crud.create_art_object("Tafari Robertson", "The Fresh Prince of The Black 90s (2022)", "Zine", "An illustrated cultural investigation of popular sitcom, The Fresh Prince of Bel-Air, and its effects on the collective black experience in the throes of capitalism and upward mobility. American, (b.1996)","Contemporary", "/static/img/the-collection/c2/t_1.pdf", 2) #add c3, c2
a5=crud.create_art_object("Tafari Robertson", "Book Space Archive: Community Book Center, New Orleans, Louisiana (2022)", "Audio Collage, 13.59", "An audio collage created from a conversation inside the Community Book Center in New Orleans. This piece is part of a series documenting the unique experience and ambience held within Black literary space by the people who create and keep them going., American, (b.1996)","Contemporary", "/static/img/the-collection/c2/t_2.mp3",2) #add c3, c2
a6=crud.create_art_object("Tafari Robertson", "Hotep Registration Form + Literacy Test (2022)", "Administrative Forms", "A project for the self identification and collection of information on the Hotep Community across the U.S speculating the purpose and presentation of forms and their implications on information. These forms are created from imagining the minute details of a new world stemming from care and black experience first, exercising the potential mundanities of drafting, designing, and implementing the need for understanding our own communities. American, (b.1996)","Contemporary", "/static/img/the-collection/c2/t_3.pdf",2) #add c3, c2

a7=crud.create_art_object("Nelson Stevens", "Uhuru", "print", "Nelson Stevens (American, born 1938). Uhuru, 1971. Screenprint on paper, Sheet: 40 x 30 in. (101.6 x 76.2 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.41. artist or artist's estate (Photo: Brooklyn Museum, 2012.80.41_PS6.jpg) ","Black Arts Movement","/static/img/c3/placeholder.gif", 3) #add c3, c2
a8=crud.create_art_object("Marie Johnson Calloway", "The Winner", "print", "Marie Johnson Calloway (American, 1920 - 2018). The Winner, 1971. Mixed media (acrylic, fabric) on wood, 60 x 30 in. (152.4 x 76.2 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.19. artist or artist's estate (Photo: Brooklyn Museum, CUR.2012.80.19.jpg) ","Black Arts Movement","/static/img/c3/placeholder.gif", 3) #add c3, c2
a9=crud.create_art_object("Glenn Ligon", "[Untitled] (Crowd/The Fire Next Time)", "print", "The accumulation of crystals suggests the mass of participants in this historic event as viewed from above, while the juxtaposition of Baldwin’s words with the image of the march—separated by more than three decades—reminds us of the still-ongoing dialogue about race in America. Screenprint with coal crystals on paper, image: 12 × 18 1/8 in. (30.5 × 46 cm). Brooklyn Museum, Alfred T. White Fund, 2000.56. artist or artist's estate (Photo: Brooklyn Museum, 2000.56_transp5856.jpg)", "Contemporary Art Movement","/static/img/c3/placeholder.gif", 3) #add c3, c2

a10=crud.create_art_object("Cleveland Bellow", "George Jackson", "print", "Cleveland Bellow (American, 1946-2009). George Jackson, 1970. Screenprint on colored paper, Sheet: 23 1/2 x 17 1/2 in. (59.7 x 44.5 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.8. © artist or artist's estate (Photo: Brooklyn Museum, 2012.80.8_PS4.jpg)", "Black Arts Movement", "/static/img/c4-Cleveland-Bellow-George-Jackson.jpg", 4) #add c3, c2
a11=crud.create_art_object("Cleveland Bellow", "Untitled", "print", "Cleveland Bellow (American, 1946-2009). Untitled, 1968. Screenprint on paper, sheet: 19 1/2 x 15 1/4 in. (49.5 x 38.7 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.6. © artist or artist's estate (Photo: Brooklyn Museum, 2012.80.6_PS4.jpg)", "Black Arts Movement","/static/img/c4-Cleveland-Bellow-George-Jackson2.jpg", 4) #add c3, c2
a12=crud.create_art_object("Cleveland Bellow", "Duke", "print", "Cleveland Bellow (American, 1946-2009). Duke, 1968. Unique screenprint on two sheets of acrylic, Sheet: 28 x 22 in. (71.1 x 55.9 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.7. artist or artist's estate (Photo: Brooklyn Museum, CUR.2012.80.7.jpg) ", "Black Arts Movement", "/static/img/c4-Cleveland-Bellow-George-Jackson.jpg3",4) #add c3, c2

art_objects=[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
model.db.session.add_all(art_objects)
model.db.session.commit() 

############################################################################################################
#                                                                                                          #
#   MUSEUMS                                                                                                #
#                                                                                                          #
############################################################################################################

#create museum from json file
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

############################################################################################################
#                                                                                                          #
#   RELATED SOUNDS                                                                                         #
#                                                                                                          #
############################################################################################################

#created 1/5/23
#create related sound  later feed data in via api 

#related sounds-2.0 version: audio museum gives me or spotify embed, fake data to show proof of concept
#has musuem id hardcoded via fk
sound1=crud.create_related_sound("podcast", "7th chapel",  "gold foil walls", "lively", "/static/audio/test-door-sound.mp3", 1) #add museums ids by hand
sound2=crud.create_related_sound("song", "Luka Doncic speaks on...",  "yellow tinted scene", "jittery",  "/static/audio/test-door-sound.mp3", 2) 
sound3=crud.create_related_sound("playlist", "Words from the curator",  "Spaghetti", "novel",  "/static/audio/test-door-sound.mp3", 3)
sound4=crud.create_related_sound("commentary", "At Last",  "baloons", "n/a",  "/static/audio/test-door-sound.mp3",4) 

sounds_in_db=[sound1, sound2, sound3, sound4]
model.db.session.add_all(sounds_in_db)
model.db.session.commit() 

############################################################################################################
#                                                                                                          #
#   PATRONS                                                                                                #
#                                                                                                          #
############################################################################################################

#no need to seed too many...server will request form data patrons during restrigationa nd login on client side and theyll be saved to the db
p1=crud.create_patron("erikkaincolor", "Erikka", "Polk", "erikkaincolor@gmail.com", "1234")
p2=crud.create_patron("testpatron", "Solange", "Knowles", "artistsmus3@blackplanet.com", "1234")

patrons=[p1, p2]
model.db.session.add_all(patrons)
model.db.session.commit()  

# #hardcode test user faves for patron profile viewing
# model.p2.collection_fave.append(c2) 
# model.p2.collection_fave.append(c3) 
# model.p2.art_fave.append(a2)
# model.p2.related_sound_fave.append(sound1) 
# model.p2.museum_fave.append(67)
# model.p2.museum_fave.append(66)
# model.p2.museum_fave.append(65)

#at the end for order purposes
# add multiple rs onto 1 collection via magic var
# multiple rs id's show up on 1 coll in collections_sounds table  
 
#edit later..rmbr sounds must be commited before i can append when seeding
#via FK-hardcoded
#via assoc table
cs1= crud.create_collection_sound(1, 1)
cs2= crud.create_collection_sound(2, 2)
cs3= crud.create_collection_sound(3, 3)
cs4= crud.create_collection_sound(4, 4)
collection_sounds=[cs1, cs2, cs3, cs4]
model.db.session.add_all(collection_sounds)
model.db.session.commit()  