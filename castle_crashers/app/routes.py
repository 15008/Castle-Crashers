from flask import render_template, redirect, url_for
from app import app, db
from app.models import Orb
from app.models import Location
from app.models import Weapon

@app.route('/')
def home():
    return render_template('home.html', page_title="Home Page")

@app.route('/all_orbs')
def all_orbs():
	orbs = Orb.query.all()
	return render_template('all_orbs.html',page_title="Animal Orbs", orbs=orbs)

@app.route("/orb/<id>")
def orb_details(id):
    orb = Orb.query.filter_by(id = id).first()
    return render_template('orb_details.html', page_title="Animal Orb Details", orb=orb)

@app.route('/all_locations')
def all_locations():
	locations = Location.query.all()
	return render_template('all_locations.html',page_title="Locations", locations=locations)

@app.route("/location/<id>")
def location_details(id):
    location = Location.query.filter_by(id = id).first()
    return render_template('location_details.html', page_title="Location Details", location=location)

@app.route('/all_weapons')
def all_weapons():
	weapons = Weapon.query.all()
	return render_template('all_weapons.html',page_title="Weapons", weapons=weapons)

@app.route("/weapon/<id>")
def weapon_details(id):
    weapon = Weapon.query.filter_by(id = id).first()
    return render_template('weapon_details.html', page_title="Weapon Details", weapon=weapon)
