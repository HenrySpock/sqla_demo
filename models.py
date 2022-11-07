from flask_sqlalchemy import SQLAlchemy
# The above line was moved over from app.py.

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models go below this point. This is where we define our schema:
class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    @classmethod    
    def get_by_species(cls, species):
        return cls.query.filter_by(species=species).all()

    @classmethod
    def get_all_hungry(cls):
        return cls.query.filter(Pet.hunger > 20).all()

    def __repr__(self):
        p = self
        return f"<Pet id: {p.id }, name: {p.name}, species: {p.species}, hunger: {p.hunger}>"

    def greet(self):
        return f"Hi, I am {self.name} the {self.species}."

    def feed(self, amt=20):
        """Update hunger based off of amount."""
        self.hunger -= amt
        self.hunger = max(self.hunger, 0)

    # The most common SQLAlchemy types for use here are:
    # Integer, String(size), Text, DateTime, Float, Boolean, PickleType, LargeBinary

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Note that autoincremenet=True is a bit different than serial primary key in postgres, which this is not.
    name = db.Column(db.String(50), nullable = False, unique = False)
    species = db.Column(db.String(30), nullable = True)
    hunger = db.Column(db.Integer, nullable=False, default=20)