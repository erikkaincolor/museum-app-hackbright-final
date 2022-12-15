# "This is the server my web app runs on"

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
#call crud functions in server view functions.

# Route design
# route name = entity+ Id, + (if possible) action

# I have( 10) tables and about (9) possible pages.
# view functions: queries and creation

#Homepage:
@app.route('/') #<---endpoint is used here and for redirects
def index():
	"""Displays content of the week and maybe embedded news or the like app page directory"""
	return render_template('login.html')
    # thing=request.forms.get('key')
	# that=request.args.get('key')

# server may be running on the same '5000' port elsewhere 
# in vs code....cmd j will open any
#terminals in vscode....or restart vscode.

#redefine mvp...minimum sort of viable..proof of concept.
#what truly is the core of my app to prove its concept/identity...anything extra is sprint 2
# display most types of things in db.
# my entities/relationships/interactions....
# seed db to preload with collections and get it to view

# testing only requires 1-2 things of each type.
#connecting bootstrap table ui that im used to/ to backend? lots of jinja for loops, each for 
# loop will be thing i want to display 
# 
# ...google 'bootstrap cards'. 






# #Login:
@app.route('/login')
def login():
	"""Patron Log-in"""
	# thing=request.forms.get('key')
	# that=request.args.get('key')
	return render_template('login.html')

#Two functions in server.py for any route that involves data entry.  For example, the login page:
@app.route('/login', methods = ['POST'])
def login_data():
	"""Server request for login info from client"""
	# username=request.forms.get('uname')
    # password=request.forms.get('pword')
	# that=request.args.get('key')
	return redirect('/')  #<——redirect to homepage if no login
	# return redirect('/', username=username, password=password)  #<——redirect to homepage if no login





# #User Profile: DOESNT WORK/i wonder if this should work like collection id/INT or as a argument/VAR
# @app.route('/profile', methods = ['GET', 'POST'])
# def index3():
# 	"""Favorites (art, audio guide tours, related sounds, museums)"""
# 	# thing=request.forms.get('key')
# 	# that=request.args.get('key')
# 	return redirect('user-profile.html') #<——redirect to homepage!





#Resources: DOESNT WORK
# @app.route('/resources')
# def name():
# 	"""Proposal for audio guide standardization + Research Links"""
# 	return render_template('resources.html') #<——possible redirect to mockup





# #Mockup: DOESNT WORK
# @app.route('/near-future-study', methods = ['GET', 'POST'])
# def index5():
# 	"""Mockup of Related Sounds Repo"""
# 	# thing=request.forms.get('key')
# 	# that=request.args.get('key')
# 	return render_template('mockup.html')





# #Museum List:
@app.route('/museumdirectory', methods = ['GET', 'POST'])
def index6():
	"""describe"""
	# thing=request.forms.get('key')
	# that=request.args.get('key')
	return render_template('museums.html')





# #Collections:
@app.route('/collections', methods = ['GET', 'POST'])
def index7():
	"""curated collections for site + accompanying related sounds"""
	# thing=request.forms.get('key')
	# that=request.args.get('key')
	return render_template('collections.html')





#Individual Collection Page: HOW DO I GET TO WORK
# @app.route('/<int: collection_id>', methods = ['GET', 'POST'])
# def index8():
# 	"""Collection content that patron selected!"""
# 	# thing=request.forms.get('key')
# 	# that=request.args.get('key')
# 	return render_template('view-collection.html')





#In-Person Audio Guide Tour:
@app.route('/audio-guide', methods = ['GET', 'POST'])
def index9():
	"""MOBILE: Museum-specific audio tours, Museum-specific solo visit playlists"""
	# thing=request.forms.get('key')
	# that=request.args.get('key')
	return render_template('guide.html')



if __name__ == "__main__":
    from model import connect_to_db

    connect_to_db(app, "muse") 

    app.run(debug=True, host="0.0.0.0") #change when depolying FIX ME