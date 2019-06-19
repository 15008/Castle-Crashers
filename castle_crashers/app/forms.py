from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional, ValidationError
import app.models
from datetime import datetime

class Add_Location(FlaskForm):
    submitAL = SubmitField('submit')
    name = TextField('name', validators=[DataRequired()])
    description = TextAreaField('description')
    chapter = IntegerField('chapter', validators=[DataRequired()])
    localeType = TextField('localeType')

class Remove_Location(FlaskForm):
    submitRL = SubmitField('submit')
    name = TextField('name', validators=[DataRequired()])

#class Select_Location(FlaskForm):
#    localeType = SelectField('localeType', validator=[DataRequired()])
