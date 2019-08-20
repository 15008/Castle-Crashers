from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional, ValidationError
from app.models import Orb, Location, Weapon
from datetime import datetime

class Edit_Location(FlaskForm):
    name = TextField('name', validators=[DataRequired(message=('Name?'))])
    description = TextAreaField('description', validators=[DataRequired(message=('Elaborate please...'))])
    chapter = IntegerField('chapter', validators=[DataRequired(message=('Please enter a chapter number!'))])
    localeType = TextField('localeType', validators=[DataRequired(message=('How could an error come up?!'))])

#    def validate_name(self, name):
#        location = Location.query.filter_by(name = name.data).first()
#        print(location)
#        if location is not None:
#            raise ValidationError('Please don\'t duplicate locations')

class Edit_Weapon(FlaskForm):
    name = TextField('name', validators=[DataRequired()])
    reqItem = TextAreaField('reqItem')
    reqLevel = IntegerField('reqLevel', validators=[DataRequired()])
    mode = TextField('mode', validators=[DataRequired()])
    strength = IntegerField('strength')
    magic = IntegerField('magic')
    defense = IntegerField('defense')
    agility = IntegerField('agility')
    iceSpecial = IntegerField('iceSpecial')
    critSpecial = IntegerField('critSpecial')
    fireSpecial = IntegerField('fireSpecial')
    elecSpecial = IntegerField('elecSpecial')
    poiSpecial = IntegerField('poiSpecial')
    cost = IntegerField('cost')

class Edit_Orb(FlaskForm):
    name = TextField('name', validators=[DataRequired()])
    description = TextAreaField('description')
    cost = IntegerField('cost')
    req = TextAreaField('req')
    magicBonus = IntegerField('magicBonus')
    strengthBonus = IntegerField('strengthBonus')
    defenseBonus = IntegerField('defenseBonus')
    agilityBonus = IntegerField('agilityBonus')
    xpBonus = IntegerField('xpBonus')
