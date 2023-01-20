"model.py for creates database model for museums and audio guide project via class declarations"

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()              

#word of caution: everytime i change this...update dunder repr's too.

#############################################
#                                           #                                                           
# PATRON table + FAVES (4) assoc. tables    #                                                  
#                                           #                                                           
#############################################

class Patron(db.Model): #ONE
    """Patrons. Museum frequenters. Art lovers. Curators. Students. Docents. Older People. Babies."""
    __tablename__ = "patrons"

    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(20), nullable=False, unique=True) 
    fname = db.Column(db.String(20), nullable=False) 
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    pword = db.Column(db.String(10), nullable=False) 
    

    #magic variables, these are missing the "secondary" key + backref    
    #adam 1/5/23: it means that there isn't a relationship 
    #need these for deets pages and dynamic jinja template looping
    # object on the other side of the relationship, i.e. not creating a backref='patrons'
    collection_fave = db.relationship('Collection', secondary= 'collection_faves', lazy=True)
    art_fave = db.relationship('ArtObject', secondary= 'art_faves', lazy=True)
    related_sound_fave = db.relationship('RelatedSound', secondary='related_sound_faves', lazy=True)
    museum_fave = db.relationship('Museum', secondary= 'museum_faves', lazy=True)

    def __repr__(self):
        """Show info about patrons."""
        return f"<Patron id={self.p_id} uname={self.uname} fname={self.fname} lname={self.lname} email={self.email} pword= sike!!!!>"

#join table
class CollectionFave(db.Model): #MANY
    """Favorited collections."""
    __tablename__ = "collection_faves"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #FK to patron and collection
    patron_id = db.Column(db.Integer, db.ForeignKey('patrons.p_id'), nullable=False) 
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False) 

    #unique constraints-odd, but will prevent patrons from having multiple faves..contains two cols
    __table_args__ = (
        db.UniqueConstraint("patron_id", "collection_id", name="uc_collection_faves"),
    )

#join table
class ArtFave(db.Model): #MANY
    """Favorited art object."""
    __tablename__ = "art_faves"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #FK to patron and art object
    patron_id = db.Column(db.Integer, db.ForeignKey('patrons.p_id'), nullable=False)  
    art_id = db.Column(db.Integer, db.ForeignKey('art_objects.id'), nullable=False) 

    #unique constraints-odd, but will prevent patrons from having multiple faves
    __table_args__ = (
        db.UniqueConstraint("patron_id", "art_id", name="uc_art_faves"),
    )

#join table
class RelatedSoundFave(db.Model): #MANY
    """Favorited sounds."""
    __tablename__ = "related_sound_faves"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #FK to patron and related sound
    patron_id = db.Column(db.Integer, db.ForeignKey('patrons.p_id'), nullable=False)  
    related_sound_id = db.Column(db.Integer, db.ForeignKey('related_sounds.id'), nullable=False) 
   
    #unique constraints-odd, but will prevent patrons from having multiple faves
    __table_args__ = (
        db.UniqueConstraint("patron_id", "related_sound_id", name="uc_sound_faves"),
    )

#join table
class MuseumFave(db.Model): #MANY
    """Favorited museums."""
    __tablename__ = "museum_faves"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #FK to patron and museum
    patron_id = db.Column(db.Integer, db.ForeignKey('patrons.p_id'), nullable=False)  
    museum_id = db.Column(db.Integer, db.ForeignKey('museums.id'), nullable=False) 

    #unique constraints-odd, but will prevent patrons from having multiple faves
    __table_args__ = (
        db.UniqueConstraint("patron_id", "museum_id", name="uc_museum_faves"), 
    )




#############################################
#                                           #                                                                    #
#      COLLECTIONS table                    #                                                               #
#                                           #                                                                    #
#############################################


class Collection(db.Model): #ONE
    """Collection of art"""
    __tablename__ = "collections"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coll_category = db.Column(db.String(50), nullable=True) 
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    curator = db.Column(db.String(30), nullable=False) 
    era = db.Column(db.String(30), nullable=True)
    # num_items = db.Column(db.Integer, nullable=True) #will be 3 automatically

    # #magic variables that belong to both, but are stored in parent
    art_object = db.relationship('ArtObject', backref='collection', lazy=True) ###
    related_sound=db.relationship("RelatedSound", secondary="collections_sounds", backref='collection')

    def __repr__(self):
        """Show info about art collection."""
        return f"<Collection id={self.id} name={self.name} curator={self.curator} era={self.era}>"  





#############################################
#                                           #                                                                    #
#  RELATED SOUNDS table + CollectionSounds  #                                                               #
#                                           #                                                                    #
#############################################
class RelatedSound(db.Model):
    """Collection of related sounds"""
    __tablename__ = "related_sounds"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    medium = db.Column(db.String(50), nullable=False) 
    sound_name = db.Column(db.Text, nullable=True) 
    description = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text, nullable=True, default="...no genre, just *vibes*!")
    # weburl = db.Column(db.Text, nullable=True, default="https://audio.mfah.yourcultureconnect.com/e/afro-atlantic-histories/") #NEW
    sound_source = db.Column(db.String, nullable=True) #delete later depending on museum or cloudinary API


    #FK to museum-needs to shows up as last param in creation of relatedsound obj in crud func, hardcoded
    museum_id = db.Column(db.Integer, db.ForeignKey('museums.id'), nullable=False)

    def __repr__(self):
            """Show info about realated sounds."""
            return f"<Sound id={self.id} medium={self.medium} genre={self.genre}>" 

#association tables/arbitrary join tables ....secondary key tag in db.rela
class CollectionSound(db.Model): 
    """Collections Sounds: podcasts, audio guide tours, songs, playlists, prose, story"""
    __tablename__ = "collections_sounds"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #FK to collection-needs to shows up as last param in creation of art object crud func
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)  #not implemented
    related_sound_id = db.Column(db.Integer, db.ForeignKey('related_sounds.id'), nullable=False)  #not implemented
    
    #unique constraints-odd, but will prevent patrons from having multiple faves..contains two cols
    __table_args__ = (
        db.UniqueConstraint("collection_id", "related_sound_id", name="uc_collection_sounds"),
    )






#############################################
#                                           #                                                                    #
#      ART OBJECTS table                    #                                                               #
#                                           #                                                                    #
#############################################

class ArtObject(db.Model): 
    """Patrons. Museum frequenters. Art lovers. Curators. Students. Docents. Old People. Babies."""
    __tablename__ = "art_objects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist = db.Column(db.String(30), nullable=False)
    title = db.Column(db.Text, nullable=False, unique=True) 
    medium = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False, default="...the description for this piece is beyond words!")
    era = db.Column(db.String(30), nullable=True)
    img_path = db.Column(db.String) #delete later depending on museum or cloudinary API
    
    #FK to collection-needs to shows up as last param in creation of art object crud func
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)  

    def __repr__(self):
        """Show info about art object."""
        return f"<Art Object id={self.id} artist={self.artist} medium={self.medium}>"
   





#############################################
#                                           #                                                                    #
#      MUSEUMS table                        #                                                               #
#                                           #                                                                    #
#############################################

class Museum(db.Model): 
    """Pinacotheca"""
    __tablename__ = "museums"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    street = db.Column(db.Text, nullable=False) #NEW
    city = db.Column(db.String(20), nullable=False) #nullable=false==required=true
    state = db.Column(db.String(20), nullable=False) 
    zipcode = db.Column(db.Integer, nullable=False) #NEW
    weburl = db.Column(db.Text, nullable=False) #NEW

    #magic variables
    related_sound=db.relationship("RelatedSound", backref='museum')

    def __repr__(self):
        """Show info about museum."""
        return f"<Museum id={self.id} name={self.name} city={self.city} state={self.state}>"













def connect_to_db(app, db_name="postgresql:///muse"): 
    """Connect to database."""
    print ("I'm very much connected to the db!")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_name  
    #app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///muse"     
    app.config["SQLALCHEMY_ECHO"] = True                                    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app        
    db.init_app(app)   

if __name__ == "__main__":
    from flask import Flask
    app=Flask(__name__) #making a flask instance
    with app.app_context():
        connect_to_db(app)
  
    #magic variables for patron class
    #these are missing the "secondary" key

    # collection_fave = db.relationship('CollectionFave', backref='patron', lazy=True)
    # art_fave = db.relationship('ArtFave', backref='patron', lazy=True)
    # related_sound_fave = db.relationship('RelatedSoundFave', backref='patron', lazy=True)
    # museum_fave = db.relationship('MuseumFave', backref='patron', lazy=True)