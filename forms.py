from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, RadioField, SubmitField, SelectField
from wtforms import validators, ValidationError


class ContactForm(FlaskForm):
    name = TextField("Name of Student", [validators.Required("Please enter your name")])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField("Address")

    email = TextField("Email", [validators.Required("Please enter your email"),
        validators.Email("Please enter your email address")])
    Age = IntegerField("Age")
    language = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'Python')])
    
    submit = SubmitField("Send")