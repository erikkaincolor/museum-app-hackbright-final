"model.py for creates database model for museums and audio guide project via class declarations"

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()              

class Patron(db.Model): #ONE
    """Patrons. Museum frequenters. Art lovers. Curators. Students. Docents. Old People. Babies."""
    __tablename__ = "patrons"

    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(20), nullable=False, unique=True) 
    fname = db.Column(db.String(20), nullable=False) 
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    pword = db.Column(db.String(10), nullable=False) 
    

    #magic variables
    #these are missing the "secondary" key
    collection_fave = db.relationship('Collection', secondary= 'collection_faves', backref='patron', lazy=True)
    art_fave = db.relationship('ArtObject', secondary= 'art_faves', backref='patron', lazy=True)
    related_sound_fave = db.relationship('RelatedSound', secondary='related_sound_faves', backref='patron', lazy=True)
    museum_fave = db.relationship('Museum', secondary= 'museum_faves', backref='patron', lazy=True)
    
    # collection_fave = db.relationship('CollectionFave', backref='patron', lazy=True)
    # art_fave = db.relationship('ArtFave', backref='patron', lazy=True)
    # related_sound_fave = db.relationship('RelatedSoundFave', backref='patron', lazy=True)
    # museum_fave = db.relationship('MuseumFave', backref='patron', lazy=True)
   
    def __repr__(self):
        """Show info about patrons."""
        return f"<Patron id={self.p_id} uname={self.uname} fname={self.fname} lname={self.lname} email={self.email} pword= sike!!!!>"

#middle tables, no meaningful, needs secondary tag or 
#association tables/arbitrary join tables ....secondary key tag in db.rela <----this one
class CollectionFave(db.Model): #MANY
    """Favorited collections."""
    __tablename__ = "collection_faves"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #FK to patron and collection
    patron_id = db.Column(db.Integer, db.ForeignKey('patrons.p_id'), nullable=False) 
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False) 

    # favorite = db.relationship('Patron', backref='collectionfave', lazy=True)

class ArtFave(db.Model): #MANY
    """Favorited art object."""
    __tablename__ = "art_faves"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #FK to patron and art object
    patron_id = db.Column(db.Integer, db.ForeignKey('patrons.p_id'), nullable=False)  
    art_id = db.Column(db.Integer, db.ForeignKey('art_objects.id'), nullable=False) 

    # favorite = db.relationship('Patron', backref='artfave', lazy=True)

class RelatedSoundFave(db.Model): #MANY
    """Favorited sounds."""
    __tablename__ = "related_sound_faves"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #FK to patron and related sound
    patron_id = db.Column(db.Integer, db.ForeignKey('patrons.p_id'), nullable=False)  
    related_sound_id = db.Column(db.Integer, db.ForeignKey('related_sounds.id'), nullable=False) 
   
    # favorite = db.relationship('Patron', backref='relatedsoundfave', lazy=True)

class MuseumFave(db.Model): #MANY
    """Favorited museums."""
    __tablename__ = "museum_faves"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #FK to patron and museum
    patron_id = db.Column(db.Integer, db.ForeignKey('patrons.p_id'), nullable=False)  
    museum_fave_id = db.Column(db.Integer, db.ForeignKey('museums.id'), nullable=False) 
  
    # favorite = db.relationship('Patron', backref='museumfave', lazy=True)









class Collection(db.Model): #ONE
    """Collection of art"""
    __tablename__ = "collections"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coll_category = db.Column(db.String(50), nullable=True) 
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    curator = db.Column(db.String(30), nullable=False) 
    era = db.Column(db.String(30), nullable=True)
    num_items = db.Column(db.Integer, nullable=True)

    #magic variables that belong to both, but are stored in parent
    art_object = db.relationship('ArtObject', backref='collection', lazy=True) ###
    # museum = db.relationship('Museum', uselist=False, backref='collection', lazy=True) #uselist key bc this relationship is 1:1

    #magic variables that belong to both, but are stored in parent
    related_sound=db.relationship("RelatedSound", secondary="collections_sounds", backref='collection')

    def __repr__(self):
        """Show info about art collection."""
        return f"<Collection id={self.id} name={self.name} curator={self.curator} era={self.era} num_items= {self.num_items}>"  

class RelatedSound(db.Model):
    """Collection of related sounds"""
    __tablename__ = "related_sounds"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    medium = db.Column(db.String(20), nullable=False) 
    sound_name = db.Column(db.Text, nullable=True) 
    description = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text, nullable=True, default="...no genre, just *vibes*!")

    #FK to museum
    mus_id = db.Column(db.Integer, db.ForeignKey('museums.id'), nullable=False)
    #^^^when creating in stance, put 'museum=instance i made'

    def __repr__(self):
            """Show info about realated sounds."""
            return f"<Sound id={self.id} medium={self.medium} genre={self.genre}>" 

#association tables/arbitrary join tables ....secondary key tag in db.rela
class CollectionSound(db.Model): 
    """Collections Sounds: podcasts, audio guide tours, songs, playlists, prose, story"""
    __tablename__ = "collections_sounds"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #FK to collection and related sound
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)  
    related_sound_id = db.Column(db.Integer, db.ForeignKey('related_sounds.id'), nullable=False) 
    








class ArtObject(db.Model): 
    """Patrons. Museum frequenters. Art lovers. Curators. Students. Docents. Old People. Babies."""
    __tablename__ = "art_objects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist = db.Column(db.String(30), nullable=False)
    title = db.Column(db.Text, nullable=False, unique=True) 
    medium = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False, default="...the description for this piece is beyond words!")
    era = db.Column(db.String(20), nullable=True)
    
    #FK to collection
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)  

    def __repr__(self):
        """Show info about art object."""
        return f"<Art Object id={self.id} artist={self.artist} medium={self.medium}>"
   







class Museum(db.Model): 
    """Pinacotheca"""
    __tablename__ = "museums"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    city = db.Column(db.String(20), nullable=False) #nullable=false==required=true
    state = db.Column(db.String(20), nullable=False) 
    country = db.Column(db.String(30), nullable=False)

    #FK to collections-not doing this anymore!
    # collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)  

    #magic variables
    related_sound=db.relationship("RelatedSound", backref='museum')

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
    with app.app_context():
        connect_to_db(app)
  

#these below are in seed file already
    # db.create_all() 
    # connect_to_db(app, "muse") #<---this is what demo had, but didnt work for me
    # connect_to_db(app) 

    # patron=Patron(uname='e', fname='ee', lname='p', email='test@test.com', pword='1234') 
    # patron1=Patron(uname='er', fname='ew', lname='p', email='test@test.com', pword='12349') 
    
    # c1 = Collection(coll_category="paint",name="paintings",description="words go here",curator="someone")
    # c2 = Collection(coll_category="drawing",name="paintings by e",description="words go here too",curator="someone else")

    # m1=Museum(name='Houston Museum of African American Culture', city='Houston', state='TX', country='USA') #removed 'collection=c1'
    # m2=Museum(name='Museum of Fine Arts', city='Houston', state='TX', country='USA')

    # sound1=RelatedSound(medium="podcast", sound_name="7th chapel",  description="gold foil walls", museum=m1) #add m3, m2
    # sound2=RelatedSound(medium="song", sound_name="Luka Doncic speaks on...",  description="yellow tinted scene", museum=m1) #add m3, m2

    # a1=ArtObject(artist="M Angelo", title="7th chapel", medium="paint", description="gold foil walls", collection=c1) #add c3, c2
    # a2=ArtObject(artist="Calder", title="Homerun", medium="sculpture", description="oil on cieling", collection=c2) #add c3, c2

    # instances=[patron, patron1, c1, c2, a1, a2, m1, m2]
    # db.session.add_all(instances) 
    # db.session.commit()