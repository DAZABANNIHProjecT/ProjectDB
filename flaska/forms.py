import wtforms.validators
from flask_wtf import FlaskForm
from wtforms import EmailField, FileField, MultipleFileField, SelectField, SelectMultipleField, StringField, \
    SubmitField, BooleanField, PasswordField, IntegerField, DateField, TelField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, InputRequired, EqualTo


class FlatForm(FlaskForm):
    floor = IntegerField("floor: ")
    area = IntegerField("Area: ")
    price = IntegerField("price: ")
    rooms = SelectField("Rooms:", choices=[1, 2, 3, 4, 5])
    phone_number = IntegerField("Enter your phone number: ")
    street = StringField("Enter street: ")
    parking = SelectField("Enter number of parkings: ", choices=[0, 1, 2, 3])
    playground = SelectField("Enter number of playgrounds: ", choices=[0, 1, 2, 3])
    floors_count = IntegerField("Enter number of floors: ")
    number = IntegerField("Enter your passport number: ")
    birth_date = DateField("Enter your birth date: ")
    distance_underground = IntegerField("Enter distance to nearest underground: ")
    distance_bus_stop = IntegerField("Enter distance to nearest bus stop: ")
    photo = FileField("Upload photoes")
    submit = SubmitField("Add")



class LoginForm(FlaskForm):
    login = StringField("Login ", [
        wtforms.validators.Length(1, 20, "Логин должен быть длиной от 1 до 20 символов"),
        wtforms.validators.Regexp("[a-zA-Z0-9_]+", message="Логин должен состоять из латинских букв и цифр")
    ])
    pwd = PasswordField("Password ")
    submit = SubmitField("Submit")


class ApplicationForm(FlaskForm):
    phone_number = IntegerField("Phone ")
    email = EmailField("Email ")
    letter = TextAreaField("Letter ")
    submit = SubmitField("Submit")


class RegistrationForm(FlaskForm):
    login = StringField("Login ")
    # phone_number = StringField("Phone number ")
    psw = PasswordField("Password ", [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    psw2 = PasswordField("Repeat password ")
    submit = SubmitField("Submit")


class ClientBuyForm(FlaskForm):
    phone_number = IntegerField("Phone number ")
    email = EmailField("Email ")
    type_of_deal = SelectMultipleField(choices=['rent', 'sale'])
    client_price = IntegerField('Enter your price ')
    submit = SubmitField("Submit")


class CompanyBuyForm(FlaskForm):
    taxpayer_identification_number = IntegerField('Enter your taxpayer identification number ')
    contact_information = EmailField("Enter contact information (email)")
    company_price = IntegerField('Enter your price ')
    submit = SubmitField("Submit")


class RegistrationTempForm(FlaskForm):
    login = StringField("Login ")
    type_user = SelectField(choices=['owner', 'client'])
    psw = PasswordField("Password ", [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    psw2 = PasswordField("Repeat password ")
    submit = SubmitField("Submit")


class ReportForm(FlaskForm):
    status = SelectField(choices=['done', 'unfinished'])
    report_content = TextAreaField("Content ")
    submit = SubmitField("Submit")


class RateForm(FlaskForm):
    mark = SelectField(choices=[1, 2, 3, 4, 5])
    feedback_message = TextAreaField("Write down some comments")
    submit = SubmitField("Submit")
