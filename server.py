"This is the server my web app runs on"

from flask import (Flask, render_template, request, session, redirect, url_for)
import crud
from jinja2 import StrictUndefined 
from data.model import connect_to_db, db 
import os

app = Flask(__name__)
app.jinja_env.undefined=StrictUndefined
app.secret_key=os.environ['APP_SECRET']
# app.config['SECRET_KEY'] = 'GDtfDCFYjD'
#site map
################################################################################################
#   -num- -done?-   -route-                
    # 1     x        # http://10.0.90:5000/                         # Landing page
    # 2     x        # http://10.0.90:5000/login                    # Patron login
    # 3     x        # http://10.0.90:5000/profile/                 # Patron profile page
    # 4     x        # http://10.0.90:5000/register                 # Register now!
    # 5     x        #      /api/museum-faves               x4      # Patron's fave art objects, collections, museums and sounds
    # 6     x        # http://10.0.90:5000/museumdirectory          # View all museums
    # 7     x        #     /museumdirectory/<museum_id>             # View museum deets
    # 8     x        #     /museumdirectory/<audio_id>              # View sound deets

    # 9     x        # http://10.0.90:5000/collections              # View all collections
    # 10    x        #     /collections/<collection_id>             # View the art objects of one collection
    # 11    x        #     /collections/1/<artobject_id>              # View art objects deets      
    # 12    x        #     /collections/collection-sounds1          # View the sounds of one collection
    # 13    x        # http://10.0.90:5000/audio-guide              # View a list of all audio-guides
    # 15    x        #     /audio-guide/1                           # View the details of one sound             
    
###########################################################################################################

############################################################################################################
#                                                                                                          #
#                                           LANDING PAGE                                                   #
#                                      http://10.0.90:5000/                                                #
#                                                                                                          #
############################################################################################################

#works
@app.route('/')
def index():
    """Home"""

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
@app.route('/login',methods = ['POST'])
def login_prompt():
    """form input on login.html is routed here, posting form data to db"""
    uname = request.form['username'] #<---get uname from form
    pword = request.form['password'] #<---get pword from form
    session['username']= request.form['username'] #request sess obj from login.html form

    patron=crud.patron_uname_lookup(uname) #<---patron obj made via id lookup...i now can access patron attr
    if patron and patron.pword==pword:
        session['patron_id'] = patron.p_id #logged in user is found in db, and theyre info is now stored in this dict
        return redirect("/profile")

    else:
        return redirect('/login')

#works
@app.route('/logout')
def logout():
    """click event link on base.html nav-item is routed here, posting response to db"""
    if "patron_id" in session: #looking for particular key in dict-like ses obj as a string
        session.clear()
        return render_template("/logout-success.html")
    else:
        return redirect(url_for('view_login'))
################################################################################################################
################################################################################################################

#works
@app.route("/profile")
def view_patron_page():
    """shows name and info, and links to collections, art, sounds and museums patron favorited"""
    if not "patron_id" in session: #logged in or not depends on this session dict from login
        return redirect('/login') 
    p_id=session['patron_id'] #storing session data in a variable
    patron=crud.patron_id_lookup(p_id) #<---patron obj made via id lookup...i now can access patron attr
    return render_template("patron-profile.html", patron=patron)
















############################################################################################################
#                                                                                                          #
#                                          PATRON FAVORITES                                                #
#                                                                                                          #
############################################################################################################

#works
@app.route('/api/museum-faves')
def add_m_faves_to_profile():
    """show museum fave on patron deets page, use magic var museum_fave from patron class"""
    p_id=session['patron_id'] #storing session data in a variable
    crud.get_m_fave_by_pid(p_id) #<---museumfave obj made via p_id lookup...i now can access patron.museum_fave attr


# works
@app.route('/api/collection-faves')
def add_c_faves_to_profile():
    """show collection fave on patron deets page, use magic var collection_fave from patron class"""
    p_id=session['patron_id']
    crud.get_c_fave_by_pid(p_id)
  

# works
@app.route('/api/art-faves')
def add_a_faves_to_profile():
    """show art fave on patron deets page, use magic var art_fave from patron class"""
    p_id=session['patron_id']
    crud.get_a_fave_by_pid(p_id) 

# works
@app.route('/api/sounds-faves')
def add_s_faves_to_profile():
    """show sounds fave on patron deets page, use magic var related_sound_fave from patron class"""
    p_id=session['patron_id'] 
    crud.get_s_fave_by_pid(p_id) 








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
@app.route('/register',methods = ['POST']) 
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
        # flash("A user with that username exists. Try again please.")
        # figure out bs or js equal
        return redirect('/register')
    elif patron_obj2: #if email is in db, error
        # flash("A user with that email exists. Try again please.")
        return redirect('/register')
    else: #if email or uname is not in db, create account
        new_user=crud.create_account(uname, fname, lname, email, pword)
        db.session.add(new_user) #add new user to db
        db.session.commit() #save forever
        # flash("Your account was created successfully and you can now log in.")
        return redirect('/login')









############################################################################################################
#                                                                                                          #
#                                           FAVORITES                                                      #
#                                       /profile/art-fave-1                                                #
#                                                                                                          #
############################################################################################################

# works
@app.route("/museumdirectory/<int:museum_id>/museumfavorites", methods = ["POST"])
def add_m_fave(museum_id):
    """letse patron add museum fave on profile page, posts button event 'answer' to db"""
    current_users_uname=session.get("username") #username needed for favoriting
    response={1:"success"}
    if current_users_uname is None:
        return {"status":"FAIL"}
    else:
        patron = crud.patron_uname_lookup(current_users_uname) #create patron obj via uname lookup
        museum_fave=crud.create_museum_fave(patron.p_id, museum_id)  #create museum_fave obj
        db.session.add(museum_fave) #add it to db
        db.session.commit() #save it forever
    return response

#works
@app.route("/museumdirectory/<int:museum_id>/removemuseumfavorites", methods = ["POST"])
def del_m_fave(museum_id):
    """delete museum fave on museum deets page, posts button event 'answer' to db"""
    response={1:"success"}
    current_users_uname=session.get("username") #username needed for unfavoriting
    
    if current_users_uname is None:
        print("Not logged in")    
    else:
        museum_fave=crud.get_m_fave_delete(session["patron_id"], museum_id)
        db.session.delete(museum_fave)
        db.session.commit() 
    return response

#######################################################

#works
@app.route("/collections/<int:collection_id>/collectionfavorites", methods = ["POST"]) 
def add_c_fave(collection_id):
    """create collection fave on profile page, posts button event 'answer' to db"""
    response={1:"success"}
    current_users_uname=session.get("username") 
    if current_users_uname is None:
        return {"status": "FAIL"}
    else:
        patron = crud.patron_uname_lookup(current_users_uname) 
        collection_fave=crud.create_collection_fave(patron.p_id, collection_id)
        db.session.add(collection_fave)
        db.session.commit()
    return response

#works
@app.route("/collections/<int:collection_id>/removecollectionfavorites", methods = ["POST"]) 
def del_c_fave(collection_id):
    """delete collection fave on profile page, posts button event 'answer' to db"""
    current_users_uname=session.get("username") 
    response={1:"success"}
    if current_users_uname is None:
        print("Not logged in")
    else:
        collection_fave=crud.get_c_fave_delete(session["patron_id"], collection_id)
        db.session.delete(collection_fave)
        db.session.commit()
    return response

#######################################################

# works
@app.route("/<int:sound_id>/soundfavorites", methods = ["POST"])
def add_s_fave(sound_id):
    """add sound fave on patron profile, posts button event 'answer' to db"""
    current_users_uname=session.get("username")
    response={1:"success"}
    if current_users_uname is None:
        return {"status":"FAIL"}
    else:
        patron = crud.patron_uname_lookup(current_users_uname) 
        related_sound_fave=crud.create_sound_fave(patron.p_id, sound_id) 
        db.session.add(related_sound_fave)
        db.session.commit() 
    return response

# works
@app.route("/<int:sound_id>/removesoundfavorites", methods = ["POST"])
def del_s_fave(sound_id):
    """delete sound fave on profile, posts button event 'answer' to db"""
    response={1:"success"}
    current_users_uname=session.get("username")
    
    if current_users_uname is None:
        print("Not logged in")    
    else:
        related_sound_fave=crud.get_s_fave_delete(session["patron_id"], sound_id)
        db.session.delete(related_sound_fave)
        db.session.commit() 
    return response

###############################################

# works
@app.route("/<int:art_id>/artfave", methods = ["POST"]) 
def add_a_fave(art_id):
    """create art fave on patron profile page, posts button event 'answer' to db"""
    response={1:"success"}
    current_users_uname=session.get("username") 
    if current_users_uname is None:
        return {"status":"FAIL"} 
    else:
        patron = crud.patron_uname_lookup(current_users_uname) 
        art_fave=crud.create_art_fave(patron.p_id, art_id) 
        db.session.add(art_fave)
        db.session.commit()
    return response

# works
@app.route("/<int:art_id>/removeartfave", methods = ["POST"]) 
def del_a_fave(art_id):
    """delete art fave on patron profile page, posts button event 'answer' to db"""
    current_users_uname=session.get("username") 
    response={1:"success"}
    if current_users_uname is None:
        print("Not logged in")    
    else:
        art_fave=crud.get_a_fave_delete(session["patron_id"], art_id)
        db.session.delete(art_fave)
        db.session.commit()
    return response











############################################################################################################
#                                                                                                          #
#                               MUSEUMS PAGE + detail page                                                 #
#                           http://10.0.90:5000/museumdirectory                                            #
#                               /museumdirectory/museum-1                                                  #
#                                                                                                          #
############################################################################################################

# works
@app.route('/museumdirectory')
def view_museums():
    """view museum table list"""
    museums = crud.get_museums()
    return render_template('museums.html', museums=museums)

# works
@app.route('/museumdirectory/<id>')
def lone_museum(id):
    """individual museum page with related sounds"""
    museum=crud.get_museum_by_id(id)
    sound=crud.get_sound_by_museum_id(id)
    return render_template('museum-details.html', museum=museum, sound=sound)









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
@app.route('/collections')
def view_collections():
    """view collections table list""" 
    collections = crud.get_collections()
    return render_template('collections.html', collections =collections)

# works
@app.route('/collections/<id>')
def lone_collection(id): 
    """collection details page"""
    collection= crud.get_collection_id(id)
    art=crud.get_art_by_coll_id(id) 
    return render_template('collection-details.html', collection=collection, art=art)

# works
@app.route('/art/<int:id>') 
def lone_art(id):
    """art deets"""
    arts= crud.get_art_by_id(id)
    return render_template('art-object-details.html', arts=arts)












############################################################################################################
#                                                                                                          #
#                               AUDIO GUIDE + detail page                                                  #
#                             http://10.0.90:5000/audio-guide                                              #
#                                   /audio-guide/1                                                         #
############################################################################################################

# works
@app.route('/audio-guides')
def view_audio_guides():
    """MOBILE IN PERSON XP: view audio guides list"""
    sounds = crud.get_sounds()
    return render_template('guide.html', sounds=sounds)

# works
#Individual Audio Guide Page: 
@app.route('/audio-guides/<int:id>') #/sound1
def lone_audio_guide(id):
    """the audio tours...the playlists....the Ted Talks, the community commentary, etc"""
    sound= crud.get_sound_by_id(id)
    return render_template('guide-details.html', sound=sound)








if __name__ == "__main__":
    # from model import connect_to_db
    connect_to_db(app)
    app.run(host="0.0.0.0", port=5005) #change when deploying FIX ME
    # i don’t want the Flask app in debug mode..its a big security hole
    # Changing app.run(debug=True) to app.run()