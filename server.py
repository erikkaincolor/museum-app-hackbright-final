# "This is the server my web app runs on"

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
#jsonify is used for what again?
import crud
from jinja2 import StrictUndefined #<-----used where?
#import os
#import requests

app = Flask(__name__)
# app.jinja_env.undefined = jinja2.StrictUndefined
app.secret_key = 'RANDOM SECRET KEY' #key doesnt matter it just needs one


################################################################################################

#routes: i have 10 tables, but 13 routes seem excessive
#     ...is there a way to prepend 'art-fave' to the front of an id in a route?
#     ...or some sort of sticky container with border that is scrollable?
#   -num- -done?-   -route-                
    # 1             # http://10.0.90:5000/                      # Landing page
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








# 1     # http://10.0.90:5000/                      # Landing page
@app.route('/')
def index():
    """Displays content of the week and maybe embedded news or the like app page directory"""

    return render_template('index.html')
#has navigation to patron profile, museum list, collection list, audio guide list    
    
    # thing=request.forms.get('key')
# 	# that=request.args.get('key')



















#2     # http://10.0.90:5000/login                 # Users can log in with their account credentials
@app.route('/login')
def view_login():
	"""Patron Log-in, has form on this page....only logged in patrons can favorite items"""
	return render_template('login.html')


@app.route('/login',methods=['POST'])
def login_prompt():
    """Server request for login info from client"""
    username = request.form['username']
    password = request.form['password']
    #need the db trip explained here...form validation

    patron=crud.patron_uname_lookup(username) #<---this takes form input to db....makes the function return a patron obj, i now can access its attr

    if password == patron.pword: #if no patron id is in session, they need to get logged in 
        #password of patron w/ specific login is checked against twhat the db has for it
        session['patron_id'] = patron.p_id #logged in or not depends on where session is globally/locally
        flash(f'Logged in as {username}') #<---doesnt work
        return redirect('/profile/<int:p_id>')
    #the session is like an identifier...my gmail vs someone elses

    else:
        flash('Wrong password! Try again please.') #<---doesnt work
        return redirect('/login')
	

        # session['current_user'] = username, for where i want it to show up again




















# 5     #     /profile/patron1/art-fave-1           # Users that have logged in can fave art objects, collections, museums and sounds....use cards, art_fave_id, coll_fave id, museum_fave_id, sound_fave_id  
# @app.route('/login',methods=['POST'])
# def view_faves():
#     """Server request for login info from client"""
#     username = request.form['username']
#     password = request.form['password']

#     if art_fave == '1234':
#         session['current_user'] = username
#         flash(f'Logged in as {username}')
#         return redirect('/')

#     else:
#         flash('Wrong password!')
#         return redirect('/login')

#include username identity sessions



























# 3     # http://10.0.90:5000/patron/p1             # View the details of one patron (a.k.a. the user’s profile page)

#User Profile: DOESNT WORK/i wonder if this should work like collection id/INT or as a argument/VAR
@app.route('/profile/<int:p_id>', methods = ['GET', 'POST'])
def view_patron_page(p_id):
    """shows name and info"""
    patron=crud.patron_id_lookup(p_id) #.first() fetched this record object via id
    session['patron-id'] = patron.p_id #this for telling the profil page its a user
    username = request.cookies['username']
    print(patron)
    return render_template('patron-profile.html', patron=patron, username=username) 
    # return redirect('/profile/{patron.p_id}', patron=patron, username=username) 
    # return redirect('/profile/<int:p_id>', patron=patron, username=username) 


# #Individual Patrons faves Page: HOW DO I GET TO WORK
# @app.route('/profile/<patron-id>/art-fave/<art_fave_id>', methods = ['GET', 'POST'])
# def view_patrons_art_fave():
# 	"""Favorites (art, audio guide tours, related sounds, museums)"""
# 	# thing=request.forms.get('key')
# 	# that=request.args.get('key')
# 	return redirect('profile/art-fave-1.html') 

# #^^^do i need a view function per favorite category? or is this a click evt card situation?
# # def view_patrons_art_fave():
# # def view_patrons_coll_fave():
# # def view_patrons_museum_fave():
# # def view_patrons_related_sounds_fave():






























# 6     # http://10.0.90:5000/museumdirectory       # View a list of all museums

# #Museum List:
# @app.route('/museumdirectory', methods = ['GET', 'POST'])
# def view_museum():
# 	"""view museum table list with static header"""
#   collections = crud.get_collection()
#   return render_template('museums.html', thing_i_want_to_view =collections)


# 7     #     /museumdirectory/museum-1             # Click evt allows u to view the details of one museum

# #Individual Museum Page:
# @app.route('/museumdirectory/museum-<int: museum_id>', methods = ['GET', 'POST'])
# def lone_museum():
# 	"""individual museum page"""

# 	return redirect('/museumdirectory/museum-3')





































# 8     # http://10.0.90:5000/collections           # View a list of all collections
# @app.route('/collections')
# def view_collections():
#     """as a patron i want to view a list of all Collections""" 
#     collections = crud.get_collection()
#     return render_template('collections.html', thing_i_want_to_view =collections)






# 9     #     /collections/1                        # Click evt allows u to view the details of one collection
# 10    #     /collections/1/artobject-1            # Click evt allows u to view the details of one art object 
# 11    #     /collections/collection-sounds1       # Click evt allows u to view the details of one sound

# #Individual Collection Page: HOW DO I GET TO WORK
# # @app.route('/<int: collection_id>', methods = ['GET', 'POST']) #/c1 pr /1
# @app.route('/collections/<int: collection_id>') #/c1 pr /1 ALSO need to pass it in as a parameter to the view func
# def lone_collection(collection_id): #it eing the url also passes it to the function
#     """Collection content that patron selected!"""
#     collection_id= crud.get_collection_by_id(int(collection_id))
#     collection=collection_id.first()
#     return redirect('/collections/collection-3')
	
#     # thing=request.forms.get('key')
# 	# that=request.args.get('key')
#     #use crud and collection id 

# #Individual Collection's Art Object Page:
# @app.route('/collections/collection-<int: collection_id>/art-object-<art_object_id>') #/c1 pr /1 ALSO need to pass it in as a parameter to the view func
# def lone_collection_art(art_object_id): #it being the url also passes it to the function
#     """Collection content that patron selected!"""

#     return redirect('/collections/collection-1/art-object-23')

# #Individual Collection's Related Sounds Page: 
# @app.route('/collections/collection-<int: collection_id>/art-object-<art_object_id>') #/c1 pr /1 ALSO need to pass it in as a parameter to the view func
# def lone_collection_sounds(related_sound_id): #it being the url also passes it to the function
#     """Collection content that patron selected!"""

#     return redirect('/collections/collection-1/sound-42')  
	


































# 12    # http://10.0.90:5000/audio-guide           # View a list of all related sounds to a museum

# #Audio Guide Page:
# @app.route('/audio-guide', methods = ['GET', 'POST'])
# def view_audio_guides():
# 	"""MOBILE IN PERSON XP: Museum-specific audio tours, Museum-specific solo visit playlists"""

    # collections = crud.get_collection()
    # return render_template('guide.html', thing_i_want_to_view =collections)



# 13    #     /audio-guide/1                        # Click evt allows u to view the details of one sound

# #Individual Audio Guide Page: 
# #@app.route('/<int: related_sound_id>', methods = ['GET', 'POST']) #/sound1
# @app.route('/audio-guide/related-sound<int: related_sound_id>', methods = ['GET', 'POST'])
# def lone_audio_guide():
# 	"""..the audio tours...the playlists"""

# 	return redirect('/audio-guide/related-sound/1')
#     #or
#     #return redirect('/audio-guide/related-sound1')
















if __name__ == "__main__":
    from model import connect_to_db

    # connect_to_db(app, "muse") 
    connect_to_db(app)

    app.run(debug=True, host="0.0.0.0") #change when depolying FIX ME




