# "This is the server my web app runs on"

from flask import Flask
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)


# # Route design
# # route name = entity+ Id, + (if possible) action

# # I have( 10) tables and about (9) possible pages.
# # view functions: queries and creation

# #Homepage:
# @app.route('/')
# def index():
# 	"""Displays content of the week and maybe embedded news or the like app page directory"""
# 	thing=request.forms.get('key')
# 	that=request.args.get('key')
# 	return redirect('index.html', var=thing)


# #Login:
# @app.route('/login', methods = ['GET', 'POST'])
# def index():
# 	"""Patron Log-in"""
# 	thing=request.forms.get('key')
# 	that=request.args.get('key')
# 	return render_template('login.html', var=thing)
# 	#return redirect('login.html', var=thing)  #<——redirect to homepage if no login





# #User Profile:
# @app.route('/profile', methods = ['GET', 'POST'])
# def index():
# 	"""Favorites (art, audio guide tours, related sounds, museums)"""
# 	thing=request.forms.get('key')
# 	that=request.args.get('key')
# 	return redirect('user-profile.html', var=thing) #<——redirect to homepage!





# #Resources:
# @app.route('/resources', methods = ['GET', 'POST'])
# def func_name():
# 	"""Proposal for audio guide standardization + Research Links"""
# 	thing=request.forms.get('key')
# 	that=request.args.get('key')
# 	return render_template('resources.html', var=thing) #<——possible redirect to mockup





# #Mockup:
# @app.route('/near-future-study', methods = ['GET', 'POST'])
# def index():
# 	"""Mockup of Related Sounds Repo"""
# 	thing=request.forms.get('key')
# 	that=request.args.get('key')
# 	return render_template('mockup.html', var=thing)





# #Museum List:
# @app.route('/museumdirectory', methods = ['GET', 'POST'])
# def index():
# 	"""describe"""
# 	thing=request.forms.get('key')
# 	that=request.args.get('key')
# 	return render_template('museums.html', var=thing)





# #Collections:
# @app.route('/collections', methods = ['GET', 'POST'])
# def index():
# 	"""curated collections for site + accompanying related sounds"""
# 	thing=request.forms.get('key')
# 	that=request.args.get('key')
# 	return render_template('collections.html', var=thing)





# #Individual Collection Page:
# @app.route('/<int: collection_id>', methods = ['GET', 'POST'])
# def index():
# 	"""Collection content that patron selected!"""
# 	thing=request.forms.get('key')
# 	that=request.args.get('key')
# 	return render_template('view-collection.html', var=thing)





# #In-Person Audio Guide Tour:
# @app.route('/audio-guide', methods = ['GET', 'POST'])
# def index():
# 	"""MOBILE: Museum-specific audio tours, Museum-specific solo visit playlists"""
# 	thing=request.forms.get('key')
# 	that=request.args.get('key')
# 	return render_template('guide.html', var=thing)



# if __name__ == "__main__":
#     from model import connect_to_db

#     connect_to_db(app, "muse") 

#     app.run(debug=True, host="0.0.0.0") #change when depolying FIX ME