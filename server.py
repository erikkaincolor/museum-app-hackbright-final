# "This is the server my web app runs on"

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
import crud
from jinja2 import StrictUndefined #setting to make it throw errors for undefined variables
#import os <-----may not need 
#import requests <----is this diff from flask request object?

app = Flask(__name__)
app.jinja_env.undefined=StrictUndefined
app.secret_key = 'RANDOM SECRET KEY' #key doesnt matter it just needs one

################################################################################################
#   -num- -done?-   -route-                
    # 1             # http://10.0.90:5000/                      # Landing page with buttons!
    # 2             # http://10.0.90:5000/login                 # Users can log in with their account credentials
    # 3             # http://10.0.90:5000/patron/p1             # View the details of one patron (a.k.a. the user’s profile page)
    # 5             #     /profile/patron1/art-fave-1           # Users that have logged in can fave art objects, collections, museums and sounds....use cards, art_fave_id, coll_fave id, museum_fave_id, sound_fave_id  
    # 6     x        # http://10.0.90:5000/museumdirectory       # View a list of all museums
    # 7             #     /museumdirectory/museum-1             # Click evt allows u to view the details of one museum
    # 8     x        # http://10.0.90:5000/collections           # View a list of all collections
    # 9             #     /collections/1                        # Click evt allows u to view the details of one collection
    # 10            #     /collections/1/artobject-1            # Click evt allows u to view the details of one art object 
    # 11            #     /collections/collection-sounds1       # Click evt allows u to view the details of one sound
    # 12    x        # http://10.0.90:5000/audio-guide           # View a list of all related sounds to a museum
    # 13            #     /audio-guide/1                        # Click evt allows u to view the details of one sound              
################################################################################################

# - [x] Display entire collection table to screen in a list
#     - [x] Display all sounds columns when clicked
#     - [x] When clicked, display all art objects columns on individual collection page
#     - [x] Return items=show_collection
#     - [x] Show_collection=Collection.query.get all

#GOAL 2, display museum list, make clickable, and related sound:
# - [ ] Display entire museums table as a list on museums page, each is clickable
#     - [ ] Display more info on individual related_sound record per selected museum

#QTNA:
#...is there a way to prepend 'art-fave' to the front of an id in a route?
# #@app.route('/<int: related_sound_id>', methods = ['GET', 'POST']) #/sound1
# @app.route('/audio-guide/related-sound<int: related_sound_id>', methods = ['GET', 'POST'])
#...or some sort of sticky container with border that is scrollable?

############################################################################################################
#                                                                                                          #
#                                           LANDING PAGE                                                   #
#                                      http://10.0.90:5000/                                                #
#                                                                                                          #
############################################################################################################

@app.route('/')
def index():
    """Displays content of the week and maybe embedded news or the like app page directory"""

    return render_template('index.html')
# html has navigation to patron profile, museum list, collection list, audio guide list    









############################################################################################################
#                                                                                                          #
#                                      LOGIN + PATRON PROFILE                                              #
#                                     http://10.0.90:5000/login                                            #
#                                            /patron/p1                                                    #
#                                                                                                          #
############################################################################################################

@app.route('/login')
def view_login():
	"""Patron Log-in, has form on this page....only logged in patrons can favorite items"""
	return render_template('login.html')


@app.route('/login',methods=['POST'])
def login_prompt():
    """Server request for login info from client"""
    username = request.form['username']
    password = request.form['password']

    patron=crud.patron_uname_lookup(username) #<---this takes form input to db....makes the function return a patron obj, i now can access its attr

    if password == patron.pword: #if no patron id is in session, they need to get logged in 
        #password of patron w/ specific login is checked against twhat the db has for it
        session['patron_id'] = patron.p_id #logged in or not depends on where session is globally/locally
        flash(f'Logged in as {username}')#<---doesnt work
        return redirect('/profile/<int:p_id>')
    #the session is like an identifier...my gmail vs someone elses

    else:
        flash(f'Wrong password! {username}, please try again.') #<---doesnt work
        return redirect('/login')
	

        # session['current_user'] = username, for where i want it to show up again

@app.route('/profile/<int:p_id>')
def view_patron_page(p_id):
    """shows name and info"""
    patron=crud.patron_id_lookup(p_id) #.first() fetched this record object via id
    # session['patron-id'] = patron.p_id #this for telling the profil page its a user
    # username = request.cookies['username']
    return render_template('patron-profile.html', patron=patron) 

#if count of patron.art_Faves==0: render template 1, asks where are the faves or has a qoute or bob ross 
#if count of any faves > 1: show the version of patron profil with faves and show faves!

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

#get fave by id FOR NOW....i want to avoid clicking to too many pages...
#idealy it could be some sort of link type situation! art faves, collection faves, sounds and museums

# #^^^do i need a view function per favorite category? or is this a click evt card situation?
# # def view_patrons_art_fave():
# # def view_patrons_coll_fave():
# # def view_patrons_museum_fave():
# # def view_patrons_related_sounds_fave():
#filtering?








############################################################################################################
#                                                                                                          #
#                               MUSEUMS PAGE + detail page                                                 #
#                           http://10.0.90:5000/museumdirectory                                            #
#                               /museumdirectory/museum-1                                                  #
#                                                                                                          #
############################################################################################################

@app.route('/museumdirectory', methods = ['GET'])
def view_museums():
    """view museum table list with static header"""
    museums = crud.get_museums()
    return render_template('museums.html', museums=museums)

@app.route('/museumdirectory/<id>')
def lone_museum(id):
    """individual museum page"""
    museum=crud.get_museum_by_id(id)
    return render_template('museum-details.html', museum=museum)













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

@app.route('/collections', methods = ['GET', 'POST'])
def view_collections():
    """view collections table list""" 
    collections = crud.get_collections()
    return render_template('collections.html', collections =collections)



@app.route('/collections/<collection_id>') #/c1 pr /1
def lone_collection(collection_id): #it eing the url also passes it to the function
    """Collection content that patron selected!"""
    collection= crud.get_collection_id(collection_id)
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
    from model import connect_to_db
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0") #change when deploying FIX ME