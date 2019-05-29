from flask import render_template, redirect, url_for
from app import app, db
from app.models import Animal
from app.models import Level
from app.models import Weapon

@app.route('/')
def home():
    return render_template('home.html', page_title="Home Page")

@app.route('/all_animals')
def all_animals():
	animals = Animal.query.all()
	return render_template('all_animals.html',page_title="Animal Orbs", animals=animals)

@app.route("/animalorb/<id>")
def animal_details(id):
    animal = Animal.query.filter_by(id = id).first()
    return render_template('animal_details.html', page_title="Animal Orb Details", animal=animal)
