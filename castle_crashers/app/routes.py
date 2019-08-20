from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import Orb, Location, Weapon
from app.forms import Edit_Location, Edit_Orb, Edit_Weapon

#==========Main Pages==========#

@app.route('/')
def home():
    return render_template('home.html', page_title="Castle Keep")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

#==========Animal Orb Pages==========#

@app.route('/all_orbs')
def all_orbs():
	orbs = Orb.query.all()
	return render_template('all_orbs.html',page_title="Animal Orbs", orbs=orbs)

@app.route('/orb/<id>')
def orb_details(id):
    orb = Orb.query.filter_by(id = id).first()
    location = Location.query.filter_by(id = orb.locationid).first()
    return render_template('orb_details.html', page_title="Animal Orb Details", orb=orb, location=location)

@app.route('/remove_orb/<id>')
def remove_orb(id):
    Orb.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect(url_for('all_orbs'))

#==========Location Pages==========#

@app.route('/all_locations')
def all_locations():
	locations = Location.query.all()
	return render_template('all_locations.html',page_title="Locations", locations=locations)

@app.route('/location/<id>')
def location_details(id):
    location = Location.query.filter_by(id = id).first()
    return render_template('location_details.html', page_title="Location Details", location=location)

@app.route('/remove_location/<id>')
def remove_location(id):
    Location.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect(url_for('all_locations'))

@app.route('/edit_location', methods=['GET', 'POST'])
def edit_locations():
    form = Edit_Location()
    if form.validate_on_submit():
        xlocation = Location()
        xlocation.name = form.name.data
        xlocation.description = form.description.data
        xlocation.chapter = form.chapter.data
        xlocation.localeType = form.localeType.data
        db.session.add(xlocation)
        db.session.commit()
        return redirect(url_for('location_details', id=xlocation.id))
    else:
        return render_template('edit_location.html', form=form, title="Editing Location")

#==========Weapons Pages==========#

@app.route('/all_weapons')
def all_weapons():
	weapons = Weapon.query.all()
	return render_template('all_weapons.html',page_title="Weapons", weapons=weapons)

@app.route('/weapon/<id>', methods=['GET', 'POST'])
def weapon_details(id):
    weapon = Weapon.query.filter_by(id = id).first()
    location = Location.query.filter_by(id = weapon.locationid).first()
    return render_template('weapon_details.html', page_title="Weapon Details", weapon=weapon, location=location)

@app.route('/remove_weapon/<id>')
def remove_weapon(id):
    Weapon.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect(url_for('all_weapons'))
#==========Experimental Forms==========#

@app.route('/edit_location/<id>', methods=['GET', 'POST'])
def edit_location(id):
    form = Edit_Location()
    xlocation = Location.query.get(id)
    form.name.data = xlocation.name
    form.description.data = xlocation.description
    form.chapter.data = xlocation.chapter
    form.localeType.data = xlocation.localeType
    if form.validate_on_submit():
        xlocation.name = form.name.data
        xlocation.description = form.description.data
        xlocation.chapter = form.chapter.data
        xlocation.localeType = form.localeType.data
        db.session.add(xlocation)
        db.session.commit()
        return redirect(url_for('location_details', id=id))
    else:
        return render_template('edit_location.html', form=form, xlocation=xlocation, title="Editing Location")

#==========Experimental==========#

@app.route('/edit_weapon/<id>', methods=['GET', 'POST'])
def edit_weapon(id):
    form = Edit_Weapon()
    weapon = Weapon.query.filter_by(id = id).first()
    form.name.data = weapon.name
    form.reqItem.data = weapon.reqItem
    form.reqLevel.data = weapon.reqLevel
    form.mode.data = weapon.mode
    form.strength.data = weapon.strength
    form.magic.data = weapon.magic
    form.defense.data = weapon.defense
    form.agility.data = weapon.agility
    form.iceSpecial.data = weapon.iceSpecial
    form.critSpecial.data = weapon.critSpecial
    form.fireSpecial.data = weapon.fireSpecial
    form.elecSpecial.data = weapon.elecSpecial
    form.poiSpecial.data = weapon.poiSpecial
    form.cost.data = weapon.cost
    if form.validate_on_submit():
        xweapon = Weapon()
        xweapon.name = form.name.data
        xweapon.reqItem = form.reqItem.data
        xweapon.reqLevel = form.reqLevel.data
        xweapon.mode = form.mode.data
        xweapon.strength = form.strength.data
        xweapon.magic = form.magic.data
        xweapon.defense = form.defense.data
        xweapon.agility = form.agility.data
        xweapon.iceSpecial = form.iceSpecial.data
        xweapon.critSpecial = form.critSpecial.data
        xweapon.fireSpecial = form.fireSpecial.data
        xweapon.elecSpecial = form.elecSpecial.data
        xweapon.poiSpecial = form.poiSpecial.data
        xweapon.cost = form.cost.data
        db.session.add(xweapon)
        db.session.commit()
        return redirect(url_for('weapon_detail.html'))
    else:
        return render_template('edit_weapon.html', form=form, weapon=weapon, title="Editing Weapon")

@app.route('/edit_weapon', methods=['GET', 'POST'])
def edit_weapons():
    form = Edit_Weapon()
    if form.validate_on_submit():
        xweapon = Weapon()
        xweapon.name = form.name.data
        xweapon.reqItem = form.reqItem.data
        xweapon.reqLevel = form.reqLevel.data
        xweapon.mode = form.mode.data
        xweapon.strength = form.strength.data
        xweapon.magic = form.magic.data
        xweapon.defense = form.defense.data
        xweapon.agility = form.agility.data
        xweapon.iceSpecial = form.iceSpecial.data
        xweapon.critSpecial = form.critSpecial.data
        xweapon.fireSpecial = form.fireSpecial.data
        xweapon.elecSpecial = form.elecSpecial.data
        xweapon.poiSpecial = form.poiSpecial.data
        xweapon.cost = form.cost.data
        db.session.add(xweapon)
        db.session.commit()
        return redirect(url_for('weapon_detail.html', id=xweapon.id))
    else:
        return render_template('edit_weapon.html', form=form, title="Editing Weapon")

@app.route('/edit_orb/<id>', methods=['GET', 'POST'])
def edit_orb(id):
    form = Edit_Orb()
    orb = Orb.query.filter_by(id=id).first()
    form.name.data = orb.name
    form.description.data = orb.description
    form.cost.data = orb.cost
    form.req.data = orb.req
    form.magicBonus.data = orb.magicBonus
    form.strengthBonus.data = orb.strengthBonus
    form.defenseBonus.data = orb.defenseBonus
    form.agilityBonus.data = orb.agilityBonus
    form.xpBonus.data = orb.xpBonus
    if form.validate_on_submit():
        xorb = Orb()
        xorb.name = form.name.data
        xorb.description = form.description.data
        xorb.cost = form.cost.data
        xorb.req = form.req.data
        xorb.magicBonus = form.magicBonus.data
        xorb.strengthBonus = form.strengthBonus.data
        xorb.defenseBonus = form.defenseBonus.data
        xorb.agilityBonus = form.agilityBonus.data
        xorb.xpBonus = form.xpBonus.data
        db.session.add(xorb)
        db.session.commit()
        return redirect(url_for('orb_details.html', id=orb.id))
    else:
        return render_template('edit_orb.html', form=form, title="Editing Orb")

@app.route('/edit_orb', methods=['GET', 'POST'])
def edit_orbs():
    form = Edit_Orb()
    if form.validate_on_submit():
        xorb = Orb()
        xorb.name = form.name.data
        xorb.description = form.description.data
        xorb.cost = form.cost.data
        xorb.req = form.req.data
        xorb.magicBonus = form.magicBonus.data
        xorb.strengthBonus = form.strengthBonus.data
        xorb.defenseBonus = form.defenseBonus.data
        xorb.agilityBonus = form.agilityBonus.data
        xorb.xpBonus = form.xpBonus.data
        db.session.add(xorb)
        db.session.commit()
        return redirect(url_for('/orb_details/<id>', id=xorb.id))
    else:
        return render_template('edit_orb.html', form=form, title="Editing Orb")
