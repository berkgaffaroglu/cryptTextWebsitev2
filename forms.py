from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField
from wtforms.validators import Length

class encryptForm(FlaskForm):
    normalText = TextAreaField('Text', validators=[Length(min=2, max=256)])
    submit = SubmitField('Encrypt Text')

class decryptForm(FlaskForm):
    normalText = TextAreaField('Encrypted Text', validators=[Length(min=2, max=256)])
    key = StringField('Your Key', validators=[Length(min=2, max=100)])
    submit = SubmitField('Decrypt Text')