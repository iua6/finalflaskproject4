from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms import validators





class csv_upload(FlaskForm):
    file = FileField()
    submit = SubmitField()