"model.py for creates database model for museums and audio guide project via class declarations"

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()              


#i have a feeling im missing matching relationship snippets in each class

class Patron(db.Model):
    """Patrons. Museum frequenters. Art lovers. Curators. Students. Docents. Old People. Babies."""
    __tablename__ = "patrons"

    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(50), nullable=False, unique=True) 
    fname = db.Column(db.String(50), nullable=False) 
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(10), nullable=False)
    pword = db.Column(db.String(10), nullable=False) 
    
    collection_fave = db.relationship('CollectionFave', backref='patron', lazy=True)
    art_fave = db.relationship('ArtFave', backref='patron', lazy=True)
    related_sound_faves = db.relationship('RelatedSoundFave', backref='patron', lazy=True)
    museum_fave = db.relationship('MuseumFave', backref='patron', lazy=True)

    def __repr__(self):
        """Show info about patrons."""
        return f"<Patron id={self.p_id} uname={self.uname} fname={self.fname} lname={self.lname} email={self.email} pword= sike!!!!>"





class CollectionFave(db.Model): 
    """Favorited collections."""
    __tablename__ = "collection_faves"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patron_id = db.Column(db.Integer, db.ForeignKey('patron.id'), nullable=False) 
    collection_id = db.Column(db.Integer, db.ForeignKey('patron.id'), nullable=False) 

class ArtFave(db.Model): 
    """Favorited art."""
    __tablename__ = "art_faves"

    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patron_id = db.Column(db.Integer, db.ForeignKey('patron.id'), nullable=False)  
    art_id = db.Column(db.Integer, db.ForeignKey('patron.id'), nullable=False) 

class RelatedSoundFave(db.Model): 
    """Favorited sounds."""
    __tablename__ = "related_sound_faves"

    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patron_id = db.Column(db.Integer, db.ForeignKey('patron.id'), nullable=False)  
    related_sound_id = db.Column(db.Integer, db.ForeignKey('patron.id'), nullable=False) 
   
class MuseumFave(db.Model):
    """Favorited museums."""
    __tablename__ = "museum_faves"

    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patron_id = db.Column(db.Integer, db.ForeignKey('patron.id'), nullable=False)  
    museum_fave_id = db.Column(db.Integer, db.ForeignKey('patron.id'), nullable=False) 
  












class Collection(db.Model): 
    """Collection of art"""
    __tablename__ = "collections"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coll_category = db.Column(db.String(50), nullable=True) 
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    curator = db.Column(db.String(50), nullable=False) 
    era = db.Column(db.String(50), nullable=True)
    num_items = db.Column(db.Integer, nullable=True)


    art_object = db.relationship('Art_Object', backref='collection', lazy=True) ###
    museum = db.relationship('Museum', backref='collection', lazy=True) ###


    def __repr__(self):
        """Show info about art collection."""
        return f"<Collection id={self.id} name={self.name} curator={self.curator} era={self.era} num_items= {self.num_items}>"
   

class RelatedSound(db.Model):
    """Collection of related sounds"""
    __tablename__ = "related_sounds"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    medium = db.Column(db.String(50), nullable=False) 
    sound_name = db.Column(db.String(50), nullable=True) 
    description = db.Column(db.String(300), nullable=False)
    genre = db.Column(db.String(50), nullable=True, default="...no genre, just *vibes*!")

    mus_id = db.Column(db.Integer, db.ForeignKey('museum.id'), nullable=False)
    def __repr__(self):
            """Show info about realated sounds."""
            return f"<Sound id={self.id} medium={self.medium} genre={self.genre}>"
    



class CollectionSound(db.Model): 
    """Collections Sounds: podcasts, audio guide tours, songs, playlists, prose, story"""
    __tablename__ = "collections_sounds"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'), nullable=False)  
    related_sound_id = db.Column(db.Integer, db.ForeignKey('relatedsound.id'), nullable=False) 
    










class ArtObject(db.Model): 
    """Patrons. Museum frequenters. Art lovers. Curators. Students. Docents. Old People. Babies."""
    __tablename__ = "art_objects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True) 
    medium = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=False, default="...the description for this piece is beyond words!")
    era = db.Column(db.String(50), nullable=True)
    
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'), nullable=False)  

    def __repr__(self):
        """Show info about art object."""
        return f"<Art Object id={self.id} artist={self.artist} medium={self.medium}>"
   












class Museum(db.Model): 
    """Pinacotheca"""
    __tablename__ = "museums"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    city = db.Column(db.String(50), nullable=False) #nullable=false==required=true
    state = db.Column(db.String(50), nullable=False) 
    country = db.Column(db.String(50), nullable=False)

    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'), nullable=False)  
    def __repr__(self):
        """Show info about museum."""
        return f"<Museum id={self.id} name={self.name} city={self.city} state={self.state} country={self.country}>"












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
    from server import app

    #connect_to_db(app, "muse") <---this is what demo had, but didnt work for me
    connect_to_db(app) 