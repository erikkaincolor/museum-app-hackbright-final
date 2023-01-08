"This is the server my web app runs on"

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
import crud
from jinja2 import StrictUndefined 
from data.model import connect_to_db, db 
#import os <-----may not need 
#import requests <----is this diff from flask request object?

app = Flask(__name__)
app.jinja_env.undefined=StrictUndefined
app.secret_key = 'RANDOM SECRET KEY'

#site map
################################################################################################
#   -num- -done?-   -route-                
    # 1     x        # http://10.0.90:5000/                         # Landing page
    # 2     x        # http://10.0.90:5000/login                    # Patron login
    # 3     x        # http://10.0.90:5000/profile/                 # Patron profile page
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
    """Displays content of the week and maybe embedded news or the like app page directory"""
    return render_template('index.html')












############################################################################################################
#                                                                                                          #
#                                      LOGIN + PATRON PROFILE                                              #
#                                     http://10.0.90:5000/login                                            #
#                                            /profile                                                      #
#                                            /login                                                        #
#                                                                                                          #
############################################################################################################

#works
@app.route('/login')
def view_login():
	"""Patron Log-in"""
	return render_template('login.html')

#works
@app.route('/login',methods=['POST'])
def login_prompt():
    """form input on login.html is routed here, posting form data to db"""
    uname = request.form['username'] #<---get uname from form
    pword = request.form['password'] #<---get pword from form
    session['username']= request.form['username'] #request sess obj from login.html form

    patron=crud.patron_uname_lookup(uname) #<---patron obj made via id lookup...i now can access patron attr
    if patron and patron.pword==pword:
        flash(f'Logged in as {uname}')
        session['patron_id'] = patron.p_id #logged in user is found in db, and theyre info is now stored in this dict
        return redirect("/profile")

    else:
        flash("Wrong username or password, try again or create an account.")
        return redirect('/login')
        #might have to connect alert to button in form

################################################################################################################
################################################################################################################

#works
@app.route("/profile") 
def view_patron_page():
    """shows name and info"""
    if not "patron_id" in session: #logged in or not depends on this session dict from login
        return redirect('/login') 
    p_id=session['patron_id'] #storing session data in a variable
    patron=crud.patron_id_lookup(p_id) #<---patron obj made via id lookup...i now can access patron attr
    return render_template("patron-profile.html", patron=patron) 

################################################################################################################
################################################################################################################

#works but is clunky
@app.route('/api/museum-faves')
def add_m_faves_to_profile():
    """show museum fave on patron deets page"""
    p_id=session['patron_id'] #storing session data in a variable
    if not "patron_id" in session: #logged in or not depends on this session dict from login
    # if not "p_id" in session: #logged in or not depends on this session dict from login
        response2={1: "nope"}
        return response2 #to ajax req
    else: #if theyre logged in
        #using magic relationship <3 variables below via crud func.
        crud.get_m_fave_by_pid(p_id) #<---museumfave obj made via p_id lookup...i now can access patron.museum_fave attr
        response={1: "success"}
        return response 

#movie ratings app example:
# @app.route("/users/<user_id>/<rating_id>", methods=["POST"])
# def show_ratings(user_id): #DONE, for server
#     user=crud.get_user_by_id(user_id)####
#     id=user.user_id
#     answer=request.form("favorited")
#     favorite=crud.add_fave(answer)
#     #AJAX

#to do:
# @app.route('/profile/<int:p_id>/art-fave/{ArtFave.patron_id}', methods = ['GET', 'POST'])
# def view_patrons_art_fave():
#     """Favorite art"""
# 	#some type of ajax that will fulfill a trip to db to get the fave and rerender result query on page"
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
# response2={1: "success"}    
# return response 















############################################################################################################
#                                                                                                          #
#                                            REGISTER                                                      #
#                                     http://10.0.90:5000/register                                         #
#                                            /register                                                     #
#                                                                                                          #
############################################################################################################

#works
@app.route('/register')
def view_registration():
	"""Patron Registration, has form on this page....only logged in patrons can favorite items"""
	return render_template('register.html')

#works
@app.route('/register',methods=['POST']) 
def register():
    """Server request for registration info from client on registration.html page"""
    uname = request.form['uname'] #<---get uname from form
    fname = request.form['fname'] #<---get fname from form
    email = request.form['email']
    lname = request.form['lname']  
    pword = request.form['pword']
     
    patron=crud.patron_uname_lookup(uname) #<---patron obj made via uname lookup...i now can access patron attr
    patron_obj2=crud.patron_email_lookup(email)

    #form validation:
    if patron: #if uname is in db, error
        flash("A user with that username exists. Try again please.")
    elif patron_obj2: #if email is in db, error
        flash("A user with that email exists. Try again please.")
    else: #if email or uname is not in db, create account
        new_user=crud.create_account(uname, fname, lname, email, pword)
        db.session.add(new_user) #add new user to db
        db.session.commit() #save forever
        # flash("Your account was created successfully and you can now log in.")
    return redirect('/login')













############################################################################################################
#                                                                                                          #
#                                           FAVORITES                                                      #
#                                             TBD                                                          #
#                                       /profile/art-fave-1                                                #
#                                                                                                          #
############################################################################################################

#below: google how to count rows in a table?
#if count of patron.art_Faves==0: render template 1, asks where are the faves or has a qoute or bob ross 
#if count of any faves > 1: show the version of patron profil with faves and show faves!

# works
@app.route("/museumdirectory/<int:museum_id>/museumfavorites", methods=["POST"])
def add_m_fave(museum_id):
    """add museum fave on museum deets page, posts button event 'answer' to db"""
    current_users_uname=session.get("username") #username needed for favoriting
    
    if current_users_uname is None:
        flash("You must log in to favorite a museum.")
    else:
        patron = crud.patron_uname_lookup(current_users_uname) #create patron obj via uname lookup
        museum_fave=crud.create_museum_fave(patron.p_id, museum_id)  #create museum_fave obj
        db.session.add(museum_fave) #add ot to db
        db.session.commit() #save it forever
    response={1:"success"}
    return response

#works
@app.route("/museumdirectory/<int:museum_id>/removemuseumfavorites", methods=["POST"])
def del_m_fave(museum_id):
    """delete museum fave on museum deets page, posts button event 'answer' to db"""
    response={1:"success"}
    current_users_uname=session.get("username") #username needed for favoriting
    
    if current_users_uname is None:
        flash("You must log in to remove a museum as favorite.")
    else:
        # patron = crud.patron_uname_lookup(current_users_uname) #delete as soon as i test i dont need it 
        museum_fave=crud.get_m_fave_by_id(museum_id)
        db.session.delete(museum_fave)
        db.session.commit() 
    return response

#works
@app.route("/collections/<int:collection_id>/collectionfavorites", methods=["POST"]) 
def add_c_fave(collection_id):
    """create collection fave on collection deets page, posts button event 'answer' to db"""
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

#works
@app.route("/collections/<int:collection_id>/removecollectionfavorites", methods=["POST"]) 
def del_c_fave(collection_id):
    """delete collection fave on collection deets page, posts button event 'answer' to db"""
    current_users_uname=session.get("username") 
    if current_users_uname is None:
        flash("You must log in to favorite a collection.")
    else:
        # patron = crud.patron_uname_lookup(current_users_uname) 
        collection_fave=crud.get_c_fave_by_id(collection_id)
        db.session.delete(collection_fave)
        db.session.commit()
    response={1:"success"}
    return response


#WIP to be attended to after i get art objects to show up in collection!
# @app.route("/collections/<int:collection_id>/artobject/<art_id>", methods=["POST"]) #id is PK, museum_id is FK
# def add_art_fave(art_id):
#     """create art object fave on art object deets page"""
#     response={1:"success"}
#     current_users_uname=session.get("username") #checking session to see if username is in session in general 
#     if current_users_uname is None:
#         flash("You must log in to favorite an art piece.")
#         #find out the on-page replacement for this
#     else:
#         #if looged in and not favorited
#         #if looged in and favortied, be able to unfavorite
#         patron = crud.patron_uname_lookup(current_users_uname) #get patron that has uname to do id method retrieval
#         art_fave=crud.create_art_fave(patron.p_id, art_id)
#        #figure out how to only do 1x HERE
#         db.session.add(art_fave)
#         db.session.commit()
#     # return render_template("/museumdirectory/<museum_id>/museumfavorites")
#     return response

# <div class="list-group">
                
#                     {{ arts.title }}, {{ arts.artist }} {{ arts.img_path}} 
#             </div>













############################################################################################################
#                                                                                                          #
#                               MUSEUMS PAGE + detail page                                                 #
#                           http://10.0.90:5000/museumdirectory                                            #
#                               /museumdirectory/museum-1                                                  #
#                                                                                                          #
############################################################################################################

# works
@app.route('/museumdirectory', methods = ['GET'])
def view_museums():
    """view museum table list"""
    museums = crud.get_museums()
    return render_template('museums.html', museums=museums)

# works
@app.route('/museumdirectory/<id>')
def lone_museum(id):
    """individual museum page"""
    museum=crud.get_museum_by_id(id)
    return render_template("museum-details.html", museum=museum)

#









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

# works
@app.route('/collections', methods = ['GET'])
def view_collections():
    """view collections table list""" 
    collections = crud.get_collections()
    return render_template('collections.html', collections =collections)

# works
@app.route('/collections/<id>') #/c1 pr /1
def lone_collection(id): #it being the url also passes it to the function
    """Multiple Art Objects show up on Collection Details page"""
    collection= crud.get_collection_id(id)
    return render_template('collection-details.html', collection=collection)

# not yet showing art in collection deets
@app.route('/collections/<id>/art')
def art_in_collection(id):
    """doesnt render a page, just shows art...may need fetch?"""
    art=crud.get_art_by_id(id)
    # arts=crud.get_art_by_coll_id(id) #may need to query all , bc it needs to show all art
    response=art.collection_id
    # return (jsonify(response.to_json))
    return response

# lets just try to replace one singular thing! via DOM manip.

# @app.route('/collections/<id>/art')
# def art_in_collection(id):
#     """doesnt render a page, just shows art...may need fetch?"""
#     collection= crud.get_collection_id(id)
#     art=crud.get_art_by_coll_id(collection.id)
#     response=art.title #send title as response #jsonify first
#     # return (jsonify(response.to_json))
#     return response



#this may use art query .get for one art piece
# @app.route('/collections/<id>/art-object-<id>') #/c1 pr /1 ALSO need to pass it in as a parameter to the view func
# def lone_collection_art(art_object_id): #it being the url also passes it to the function
#     """Art object from particular collection"""
#     crud.get_art_by_id(id)
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