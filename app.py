from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

# This import going in the models.py file, then we import models to the app.py file:
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# The movies_example code was for testing the initial setup of SQLAlchemy. 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petshopdb'
# Track modifications are deprecated, hence the below line:
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# The following line helps show us what actual SQL call is made:
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "thekey"
app.config['DEBUG_TB_INTERCEPT_REDIERECTS'] = False 
debug = DebugToolbarExtension(app)



# This specifies that we are using postgres, and what database we are using. This has to be done first.

# --------------------------------------
# This section was moved to models.py:
# db = SQLAlchemy() 
# # The above runs SQLAlchemy and stores it to the variable db, so most commands will looke like db.[]
# db.app = app
# db.init_app(app)
# # db.app = app associates the app and the init command with he db variable 
# --------------------------------------

connect_db(app)

@app.route('/')
def list_pets():
    """Shows list of all pets in db."""
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)

@app.route('/', methods = ["POST"])
def create_pet():
    name = request.form["name"]
    species = request.form["species"]
    hunger = request.form["hunger"]
    hunger = int(hunger) if hunger else None
    # Above line exists because all inputs are strings, and we want a number.
    
    new_pet = Pet(name=name, species=species, hunger=hunger)
    db.session.add(new_pet)
    db.session.commit()

    return redirect(f"/{new_pet.id}")

@app.route("/<int:pet_id>")
def show_pet(pet_id):
    """Show details about a single pet.""" 
    pet = Pet.query.get_or_404(pet_id)
    return render_template("details.html", pet=pet)

@app.route("/species/<species_id>")
def show_pets_by_speces(species_id):
    pets = Pet.get_by_species(species_id)
    return render_template("species.html", pets=pets, species=species_id)