from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Orb
from app.models import Location
from app.models import Weapon
from app.forms import Add_Location

@app.route('/')
def home():
    return render_template('home.html', page_title="Home Page")

@app.route('/all_orbs')
def all_orbs():
	orbs = Orb.query.all()
	return render_template('all_orbs.html',page_title="Animal Orbs", orbs=orbs)

@app.route('/orb/<id>')
def orb_details(id):
    orb = Orb.query.filter_by(id = id).first()
    location = Location.query.filter_by(id = id).first()
    return render_template('orb_details.html', page_title="Animal Orb Details", orb=orb, location=location)

@app.route('/all_locations')
def all_locations():
	locations = Location.query.all()
	return render_template('all_locations.html',page_title="Locations", locations=locations)

@app.route('/location/<id>')
def location_details(id):
    location = Location.query.filter_by(id = id).first()
    return render_template('location_details.html', page_title="Location Details", location=location)

@app.route('/all_weapons')
def all_weapons():
	weapons = Weapon.query.all()
	return render_template('all_weapons.html',page_title="Weapons", weapons=weapons)

@app.route('/weapon/<id>')
def weapon_details(id):
    weapon = Weapon.query.filter_by(id = id).first()
    location = Location.query.filter_by(id = id).first()
    return render_template('weapon_details.html', page_title="Weapon Details", weapon=weapon, location=location)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    formAL = Add_Location()
    formRL = Remove_location()
    if request.method=='GET':
        return render_template('contact.html', formAL=formAL, title="Contact")
    else:
        if formAL.submitAL.data and formAL.validate():
            new_location = Location()
            new_location.name = formAL.name.data
            new_location.description = formAL.description.data
            new_location.chapter = formAL.chapter.data
            new_location.localeType = formAL.localeType.data
            db.session.add(new_location)
            db.session.commit()
            return redirect(url_for('location_details', id=new_location.id))
        else:
            return render_template('contact.html', formAL=formAL, title="Contact")
    if request.method=='GET':
        return render_template('contact.html', formRL=formRL, title="Contact")
    else:
        if formRL.submitRL.data and formRL.validate():
            want_locale = Location()
            want_locale.name = formRL.name.data
            db.session.remove(want_locale)
            db.session.commit()
            return redirect(url_for('success'))
        else:
            return render_template('contact.html', formRL=formRL, title="Contact")

#Error Handler
#@app.errorhandler(404)
#    def page_not_found(e):
#        return render_template('404.html', error=str(e))
