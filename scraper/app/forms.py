from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class CommanderSearch(FlaskForm):
    commander = StringField('Commander', validators = [InputRequired()])
    submit = SubmitField('Search')

