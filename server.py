"This is the server my web app runs on"

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
import crud
from jinja2 import StrictUndefined 
from model import connect_to_db, db 
#import os <-----may not need 
#import requests <----is this diff from flask request object?

app = Flask(__name__)
app.jinja_env.undefined=StrictUndefined
app.secret_key = 'RANDOM SECRET KEY'

################################################################################################
#   -num- -done?-   -route-                
    # 1     x        # http://10.0.90:5000/                         # Landing page
    # 2     x        # http://10.0.90:5000/login                    # Patron login
    # 3     x        # http://10.0.90:5000/patron/<p_id>            # Patron profile page
    # 4     x        # http://10.0.90:5000/register                 # Register now!
    # 5              #     /profile/1/<*artfave* id>        x4      # Patron's fave art objects, collections, museums and sounds
    # 6     x        # http://10.0.90:5000/museumdirectory          # View a list of all museums
    # 7     x        #     /museumdirectory/<museum_id>             # View the details of one museum
    # 8              #     /museumdirectory/<museum_id>/audio-guide # View sounds of one museum

    # 9, 10        ****one route will direct users to sound deets! patrons coming from one museum deets og and those coming from audio guide list page

    # 11    x        # http://10.0.90:5000/collections              # View a list of all collections
    # 12    1/2      #     /collections/<collection_id>             # View the art objects of one collection
    # 13    API      #     /collections/1/artobjects                # may be similar to register in that it displays art objects from api          
    # 14             #     /collections/1/artobjects/<art_id>       # View the details of one art object in a collection
    # 15     .25     #     /collections/collection-sounds1          # View the sounds of one collection
    # 16             # http://10.0.90:5000/audio-guide              # View a list of all sounds <- a "list" for now
    # **             #     /audio-guide/1                           # *****View the details of one sound****              
    # 14    x
################################################################################################

############################################################################################################
#                                                                                                          #
#                                           LANDING PAGE                                                   #
#                                      http://10.0.90:5000/                                                #
#                                                                                                          #
############################################################################################################

#works
@app.route('/')
def index():
    """Displays content of the week and maybe embedded news or the like app page directory, navigation to patron profile, museum list, collection list, audio guide list"""

    return render_template('index.html')














############################################################################################################
#                                                                                                          #
#                                      LOGIN + PATRON PROFILE                                              #
#                                     http://10.0.90:5000/login                                            #
#                                            /patron/p1                                                    #
#                                                                                                          #
############################################################################################################

#works
@app.route('/login')
def view_login():
	"""Patron Log-in, has form on this page....only logged in patrons can favorite items"""
	return render_template('login.html')

#works
@app.route('/login',methods=['POST']) #uses form data, form from login.html routes here
def login_prompt():
    """Server request for login info from client"""
    uname = request.form['username']
    session['username']= request.form['username'] #####################
    pword = request.form['password']

    patron=crud.patron_uname_lookup(uname) #<---i now can access its attr
    if patron and patron.pword==pword:
        flash(f'Logged in as {uname}')
        session['patron_id'] = patron.p_id #logged in or not depends on where session is globally/locally
        return redirect(f"/profile/{patron.p_id}")
    else:
        flash("Wrong username or password, try again")
        return redirect('/login')

    #the session is like an identifier...my gmail vs someone elses
	# session['current_user'] = username, for where i want it to show up again

#works
@app.route('/register',methods=['POST']) #uses form data, form from login.html routes here
def register():
    """Server request for registration info from client"""
    uname = request.form['uname']
    fname = request.form['fname']
    email = request.form['email']
    lname = request.form['lname']  
    pword = request.form['pword']
     
    patron=crud.patron_uname_lookup(uname)
    patron_obj2=crud.patron_email_lookup(email)

    if patron: #if uname is in db, error
        flash("A user with that username exists. Try again please.")
    elif patron_obj2.email: #if email is in db, error
        flash("A user with that email exists. Try again please.")
    else: #if email or uname is not in db, create account
        new_user=crud.create_account(uname, fname, lname, email, pword)
        db.session.add(new_user)
        db.session.commit()
        flash("Your account was created successfully and you can now log in.")
    return redirect('/login')

#works
@app.route("/profile/<p_id>") #works w/o "int:"
def view_patron_page(p_id):
    """shows name and info"""
    patron=crud.patron_id_lookup(p_id) 
    session['patron_id'] = patron.p_id #this for telling the profile page its a user
    # username = request.cookies['username'] ??????
    return render_template("patron-profile.html", patron=patron) 

#WIP
@app.route("/profile/<p_id>/patronfavorites", methods=["POST"]) #id is PK, museum_id is FK
def add_m_fave_to_profile(p_id):
    """show fave on patron deets page"""
    museumfave=crud.get_m_fave_by_patron_id(p_id) #museumfave obj!
    print(f"**************************THIS IS MY {museumfave.id}**********")
    return render_template("patron-profile.html", museumfave=museumfave) 


# #^^^in html, implement these faves into maybe an aside menu or a click evt card situation?
# # def add_art_fave():
# # def add_coll_fave():
# # def add_related_sounds_fave():
#filtering?


# @app.route('/profile/<int:p_id>/art-fave/{ArtFave.patron_id}', methods = ['GET', 'POST'])
# def view_patrons_art_fave():
#     """Favorite art"""
# 	#some type of ajax that will fulfill a trip to db to get the fave and rerender result query on page"
#     return redirect(f'patron-profile.html') 

# @app.route('/profile/<int:p_id>/museum-fave/{MuseumFave.patron_id}', methods = ['GET', 'POST'])
# def view_patrons_muse_fave():
#     """Favorite museums"""
#     #some type of ajax that will fulfill a trip to db to get the fave and rerender result query on page"
#     return redirect(f'patron-profile.html') 

# @app.route('/profile/<int:p_id>/collection-fave/{CollectionFave.patron_id}', methods = ['GET', 'POST'])
# def view_patrons_collection_fave():
#     """Favorite collections"""
# 	#some type of ajax that will fulfill a trip to db to get the fave and rerender result query on page"
#     return redirect(f'patron-profile.html') 

# @app.route('/profile/<int:p_id>/related-sound-fave/{RelatedSoundFave.patron_id}', methods = ['GET', 'POST'])
# def view_patrons_sound_fave():
#     """Favorite sounds"""
# 	#some type of ajax that will fulfill a trip to db to get the fave and rerender result query on page"
#     return redirect(f'patron-profile.html') 



























############################################################################################################
#                                                                                                          #
#                                           FAVORITES                                                      #
#                                             TBD                                                          #
#                                   /profile/patron1/art-fave-1                                            #
#                                                                                                          #
############################################################################################################

#    session['patron_id'] = patron.p_id #this for telling the profile page its a user
#    current_users_id=session.get("p_id") #id (not username) might be needed in view func for viewing favoriting
#    would be helpful to be logged in and print sessions dict, so far, to terminal

# need to consider before queue: id is PK, museum_id is FK, try adding a route and passing 
# in patron_id as the fk to museumfave! itll be the view functions parameter

#get fave by id FOR NOW....i want to avoid clicking to too many pages...
#idealy it could be some sort of link type situation! art faves, collection faves, sounds and museums

#below: google how to count rows in a table?
#if count of patron.art_Faves==0: render template 1, asks where are the faves or has a qoute or bob ross 
#if count of any faves > 1: show the version of patron profil with faves and show faves!

#movie ratings app example:
# @app.route("/users/<user_id>/<rating_id>", methods=["POST"])
# def show_ratings(user_id): #DONE, for server
#     user=crud.get_user_by_id(user_id)####
#     id=user.user_id
#     answer=request.form("favorited")
#     favorite=crud.add_fave(answer)
#     #AJAX







# works...it just lets u favorite multiple times smh
@app.route("/museumdirectory/<int:museum_id>/museumfavorites", methods=["POST"])
def add_m_fave(museum_id):
    """create museum fave on museum deets page"""
    response={1:"success"}
    current_users_uname=session.get("username") #username needed for favoriting
    
    if current_users_uname is None:
        flash("You must log in to favorite a museum.")
    else:
        patron = crud.patron_uname_lookup(current_users_uname)
        museum_fave=crud.create_museum_fave(patron.p_id, museum_id)
        #figure out how to only do 1x HERE
        #how to get data from client to only commit to db one time via view function python
        #how to limit it to one event click, or one evt click means add, another one means remove
        db.session.add(museum_fave)
        db.session.commit() #db.session.delete?
    return response

#this version below is a test to allow user to only favorite item 1x
# do another test to see if favorite can be removed

# @app.route("/museumdirectory/<int:museum_id>/museumfavorites", methods=["POST"]) #id is PK, museum_id is FK
# def add_m_fave(museum_id):
#     """create museum fave on museum deets page"""
#     response={1:"success"}
#     current_users_uname=session.get("username") #checking session to see if username is in session in general 
#     if current_users_uname is None:
#         flash("You must log in to favorite a museum.")
#         #find out the on-page replacement for this
#     else:
#         #if looged in and not favorited
#         #if looged in and favortied, be able to unfavorite
#         patron = crud.patron_uname_lookup(current_users_uname) #get patron that has uname to do id method retrieval
#         print(f"*****************patron={patron}*****************")
#         museum_fave=crud.create_museum_fave(patron.p_id, museum_id)
#         print(f"*****************museumid_type={type(museum_id)}*****************")
#         muse_fave= crud.lookup_muse_fave_id(patron.p_id)
#         #CODE WORKS UNTIL HERE
#         # if session['patron_id'] in muse_fave.patron_id:
#         if session['patron_id'] in muse_fave.patron_id:
#             print(f"FOUND") #IT PRINTED ;)
#             #new new
#             #look it up, verify its in there and delete
#             db.session.delete(museum_fave[1:]) #essentially, delete all but first
#             db.session.commit()
#      # return render_template("/museumdirectory/<museum_id>/museumfavorites")
#     return response


#works perfectly fine as of 12/28
@app.route("/collections/<int:collection_id>/collectionfavorites", methods=["POST"]) 
def add_c_fave(collection_id):
    """create collection fave on collection deets page"""
    response={1:"success"}
    current_users_uname=session.get("username") 
    if current_users_uname is None:
        flash("You must log in to favorite a collection.")
    else:
        patron = crud.patron_uname_lookup(current_users_uname) 
        collection_fave=crud.create_collection_fave(patron.p_id, collection_id)
        db.session.add(collection_fave)
        db.session.commit()
    return response




#WIP to be attended to after i get art objects to show up in collection!
# @app.route("/collections/<int:collection_id>/artobject/<art_id>", methods=["POST"]) #id is PK, museum_id is FK
# def add_art_fave(art_id):
#     """create art object fave on art object deets page"""
#     print("******************HIIIIIII*****************")
#     response={1:"success"}
#     current_users_uname=session.get("username") #checking session to see if username is in session in general 
#     print(f"******************current_user:{current_users_uname}*****************")
#     if current_users_uname is None:
#         flash("You must log in to favorite an art piece.")
#         #find out the on-page replacement for this
#     else:
#         #if looged in and not favorited
#         #if looged in and favortied, be able to unfavorite
#         patron = crud.patron_uname_lookup(current_users_uname) #get patron that has uname to do id method retrieval
#         print(f"*****************patron={patron}*****************")
#         art_fave=crud.create_art_fave(patron.p_id, art_id)
#         print(f"*****************museumid_type={type(art_id)}*****************")
#        #figure out how to only do 1x HERE
#         db.session.add(art_fave)
#         db.session.commit()
#     # return render_template("/museumdirectory/<museum_id>/museumfavorites")
#     return response




























############################################################################################################
#                                                                                                          #
#                               MUSEUMS PAGE + detail page                                                 #
#                           http://10.0.90:5000/museumdirectory                                            #
#                               /museumdirectory/museum-1                                                  #
#                                                                                                          #
############################################################################################################

@app.route('/museumdirectory', methods = ['GET']) #removed post on 12/28
def view_museums():
    """view museum table list with static header"""
    museums = crud.get_museums()
    return render_template('museums.html', museums=museums)

@app.route('/museumdirectory/<int:id>')
def lone_museum(id):
    """individual museum page"""
    museum=crud.get_museum_by_id(id)
    return render_template("museum-details.html", museum=museum)


























############################################################################################################
#                                                                                                          #
#                                  COLLECTIONS + detail page                                               #
#                                http://10.0.90:5000/collections                                           #
#                                     /collections/1                                                       #
#                                /collections/1/artobject-1                                                #
#                                     /collections/1                                                       #
#                               /collections/collection-sounds1                                            #
#                                                                                                          #
############################################################################################################

 #use crud and collection id 

@app.route('/collections', methods = ['GET'])
def view_collections():
    """view collections table list""" 
    collections = crud.get_collections()
    return render_template('collections.html', collections =collections)

@app.route('/collections/<id>') #/c1 pr /1
def lone_collection(id): #it eing the url also passes it to the function
    """Collection content that patron selected!"""
    collection= crud.get_collection_id(id)
    return render_template('collection-details.html', collection=collection)



# @app.route('/collections/collection-<int: collection_id>/art-object-<art_object_id>') #/c1 pr /1 ALSO need to pass it in as a parameter to the view func
# def lone_collection_art(art_object_id): #it being the url also passes it to the function
#     """Collection content that patron selected!"""
#     return redirect('/collections/collection-1/art-object-23')

# @app.route('/collections/collection-<int: collection_id>/art-object-<art_object_id>') #/c1 pr /1 ALSO need to pass it in as a parameter to the view func
# def lone_collection_sounds(related_sound_id): #it being the url also passes it to the function
#     """Collection content that patron selected!"""
#     return redirect('/collections/collection-1/sound-42')  
	


























############################################################################################################
#                                                                                                          #
#                               AUDIO GUIDE + detail page                                                  #
#                             http://10.0.90:5000/audio-guide                                              #
#                                   /audio-guide/1                                                         #
############################################################################################################

# @app.route('/audio-guides', methods = ['GET', 'POST'])
# def view_audio_guides():
# 	"""MOBILE IN PERSON XP: view audio guides list"""
    # sounds = crud.get_collection()
    # return render_template('guide.html', sounds=sounds)

# #Individual Audio Guide Page: 
# #@app.route('/<int: related_sound_id>', methods = ['GET', 'POST']) #/sound1
# def lone_audio_guide():
# 	"""..the audio tours...the playlists"""
# 	return redirect('/audio-guide/related-sound/1')
#   #or
#   #return redirect('/audio-guide/related-sound1')




























if __name__ == "__main__":
    # from model import connect_to_db
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0", port=5005) #change when deploying FIX ME




    ###before i created a successful button w/ evt listener!!
    # @app.route("/museumdirectory/<museum_id>/museumfavorites", methods=["POST"]) #id is PK, museum_id is FK
# def add_m_fave(museum_id):
#     """create museum fave on museum deets page"""
#     current_users_uname=session.get("username")
#     # favorite_status=request.form.get("favorite_status")
#     # faves=[] #empty list that i can loop over in jinja2 elsewhere?
#     #-----------> how to retrieve button click? <--------------------
#     # favorite=request.form.get("favorite") #just what the value put into that button click? this si why i want to do checkbox
#     if current_users_uname is None:
#         flash("You must log in to favorite a museum.")
#     # elif not favorite_status: #if theres no score, see if required or not
#     #     flash("Error: you didn't select a score for your rating.")
#     else:
#         patron = crud.patron_uname_lookup(current_users_uname)
        # museum_id=crud.get_museum_by_id(museum_id) #passed in from url
#         museum_fave=crud.create_museum_fave(museum_id,patron.id)
#         db.session.add(museum_fave)
#         db.session.commit()

#     # if favorite:
#     #     faves.append(favorite)
#     #     db.session.add(favorite)
#     #     db.sesion.commit()
#     # return render_template("/museumdirectory/<museum_id>/museumfavorites")
