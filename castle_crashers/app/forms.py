from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional, ValidationError
import app.models
from datetime import datetime

class Edit_Location(FlaskForm):
    name = TextField('name', validators=[DataRequired()])
    description = TextAreaField('description')
    chapter = IntegerField('chapter', validators=[DataRequired()])
    localeType = TextField('localeType')

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
