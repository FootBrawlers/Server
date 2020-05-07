from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import NumberRange
class CommandForm(FlaskForm):
    command = IntegerField('Command', validators=[NumberRange(min=0,max=2)])
    submit = SubmitField('Send Input')