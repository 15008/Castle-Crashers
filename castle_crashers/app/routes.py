from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Orb, Location, Weapon
from app.forms import Add_Location, Edit_Orb

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

@app.route('/location/<id>', methods=['GET', 'POST'])
def location_details(id):
    location = Location.query.filter_by(id = id).first()
    form = Remove_Location()
    if form.validate_on_sumbit():
        db.session.delete(location)
        db.session.commit()
        return render_template('home.html', page_title="Home Page")
    else:
        return render_template('location_details.html', page_title="Location Details", location=location, form=form)

@app.route('/all_weapons')
def all_weapons():
	weapons = Weapon.query.all()
	return render_template('all_weapons.html',page_title="Weapons", weapons=weapons)

@app.route('/weapon/<id>')
def weapon_details(id):
    weapon = Weapon.query.filter_by(id = id).first()
    location = Location.query.filter_by(id = id).first()
    return render_template('weapon_details.html', page_title="Weapon Details", weapon=weapon, location=location)

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/edit_location', methods=['GET', 'POST'])
def add_location():
    form = Add_Location()
    if form.validate_on_submit():
        new_location = Location()
        new_location.name = form.name.data
        new_location.description = form.description.data
        new_location.chapter = form.chapter.data
        new_location.localeType = form.localeType.data
        db.session.add(new_location)
        db.session.commit()
        return redirect(url_for('location_details.html', id=new_location.id))
    else:
        return render_template('edit_location.html', form=form, title="Add Location")

#@app.route('/add_weapon', method=['GET', 'POST'])
#def add_weapon():
#    form = Add_Weapon()
#    if form.validate_on_submit():
#        new_weapon = Weapon()
#        new_weapon.name = form.name.data
#        new_weapon.reqItem = form.reqItem.data
#        new_weapon.reqLevel = form.reqLevel.data
#        new_weapon.mode = form.mode.data
#        new_weapon.strength = form.strength.data
#        new_weapon.magic = form.magic.data
#        new_weapon.defense = form.defense.data
#        new_weapon.agility = form.agility.data
#        new_weapon.iceSpecial = form.iceSpecial.data
#        new_weapon.critSpecial = form.critSpecial.data
#        new_weapon.fireSpecial = form.fireSpecial.data
#        new_weapon.elecSpecial = form.elecSpecial.data
#        new_weapon.poiSpecial = form.poiSpecial.data
#        new_weapon.cost = form.cost.data
#        db.session.add(new_weapon)
#        db.session.commit()
#        return redirect(url_for('weapon_detail.html', id=new_weapon.id))
#    else:
#        return render_template('remove_weapon.html', form=form, title="Remove Weapon")

#@app.route('/remove_weapon', methods=['GET', 'POST'])
#def remove_weapon():
#    form = Remove_Weapon()
#    if form.validate_on_submit():
#        ex_weapon = Weapon.query.filter_by(name = form.name.data).first()
#        db.session.delete(ex_weapon)
#        db.session.commit()
#        return render_template('success.html', page_title="Success")
#    else:
#        return render_template('remove_weapon.html', form=form, title="Remove Weapon")

#@app.route('/edit_orb', method=['GET', 'POST'])
#def edit_orb():
#    form = Edit_Orb()
#    if form.validate_on_submit():
#        new_orb.description = form.description.data
#        new_orb.cost = form.cost.data
#        new_orb.req = form.req.data
#        new_orb.magicBonus = form.magicBonus.data
#        new_orb.strengthBonus = form.strength.data
#        new_orb.defenseBonus = form.defense.data
#        new_orb.agilityBonus = form.agilityBonus.data
#        new_orb.xpBonus = form.xpBonus.data
#        if add_data:
#            new_orb.name = form.name.data
#            db.session.add(new_orb)
#            db.session.commit()
#            return redirect(url_for('orb_detail.html', id=new_orb.id))
#        elif remove_data:
#            ex_orb = Orb.query.filter_by(name = form.name.data).first()
#            db.session.delete(ex_orb)
#            db.session.commit()
#            return render_template('success.html', page_title="Success")
#        elif update_data:
#            ex_orb.name = Orb.query.filter_by(name = form.name.data).first()
#            db.session.add(ex_orb)
#    else:
#        return render_template('edit_orb.html', form=form, title = "Edit Orbs")
