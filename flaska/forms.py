import wtforms.validators
from flask_wtf import FlaskForm
from wtforms import EmailField, FileField, MultipleFileField, SelectField, SelectMultipleField, StringField, \
    SubmitField, BooleanField, PasswordField, IntegerField, DateField, TelField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, InputRequired, EqualTo


class FlatForm(FlaskForm):
    floor = IntegerField("floor: ", [wtforms.validators.number_range(-2, 200, "В Бурдж Халифе всего 163 этажа, вы наверное, что то путаете")])
    area = IntegerField("Area: ", [wtforms.validators.number_range(0, 1000000000, "Площадь квартиры не может быть отрицательным числом, или же миллиард кв. м тоже перебор")])
    price = IntegerField("price: ", [wtforms.validators.number_range(0, 500000000000, "Цена квартиры не может быть отрицательным числом, или же 500 миллиард рублей тоже перебор")])
    rooms = SelectField("Rooms:", choices=[1, 2, 3, 4, 5])
    phone_number = StringField("Phone ", [wtforms.validators.Regexp("[8][\\d]{10}", message="Введите телефонный номер с восьмерки")])
    street = StringField("Enter street: ", [wtforms.validators.Length(0, 50, "Название улицы не должно преавшать 500 символов")])
    parking = SelectField("Enter number of parkings: ", choices=[0, 1, 2, 3])
    playground = SelectField("Enter number of playgrounds: ", choices=[0, 1, 2, 3])
    floors_count = IntegerField("Enter number of floors: ", [wtforms.validators.number_range(-2, 200, "В Бурдж Халифе всего 163 этажа, вы наверное, что то путаете")])
    number = StringField("Enter your passport number: ", [wtforms.validators.Regexp("[8][\\d]{10}", message="Введите телефонный номер с восьмерки")])
    birth_date = DateField("Enter your birth date: ")
    distance_underground = IntegerField("Enter distance to nearest underground: ", [wtforms.validators.number_range(0, 500000000000, "Расстояние не может быть отрицательным или таким большим")])
    distance_bus_stop = IntegerField("Enter distance to nearest bus stop: ", [wtforms.validators.number_range(0, 500000000000, "Расстояние не может быть отрицательным или таким большим")])
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
    phone_number = StringField("Phone ", [wtforms.validators.Regexp("[8][\\d]{10}", message="Введите телефонный номер с восьмерки")])
    email = EmailField("Email ")
    letter = TextAreaField("Letter ", [wtforms.validators.Length(0, 2000, "Приложение не должно превышать 2000 символов")])
    submit = SubmitField("Submit")


class RegistrationForm(FlaskForm):
    login = StringField("Login ", [
        wtforms.validators.Length(1, 20, "Логин должен быть длиной от 1 до 20 символов"),
        wtforms.validators.Regexp("[a-zA-Z0-9_]+", message="Логин должен состоять из латинских букв и цифр")
    ])
    phone_number = StringField("Phone ", [wtforms.validators.Regexp("[8][\\d]{10}", message="Введите телефонный номер с восьмерки")])
    psw = PasswordField("Password ", [InputRequired(), EqualTo('confirm',
                                                               message='Passwords must match')])
    psw2 = PasswordField("Repeat password ")
    submit = SubmitField("Submit")


class ClientBuyForm(FlaskForm):
    phone_number = StringField("Phone ", [wtforms.validators.Regexp("[8][\\d]{10}", message="Введите телефонный номер с восьмерки")])
    email = EmailField("Email ")
    type_of_deal = SelectMultipleField(choices=['rent', 'sale'])
    client_price = IntegerField('Enter your price ', [wtforms.validators.number_range(0, 500000000000, "Цена квартиры не может быть отрицательным числом, или же 500 миллиард рублей тоже перебор")])
    submit = SubmitField("Submit")


class CompanyBuyForm(FlaskForm):
    taxpayer_identification_number = IntegerField('Enter your taxpayer identification number '[wtforms.validators.Length(12, 12, "ИНН состоит из 12 цифр")])
    contact_information = EmailField("Enter contact information (email)")
    company_price = IntegerField('Enter your price ', [wtforms.validators.number_range(0, 500000000000, "Цена квартиры не может быть отрицательным числом, или же 500 миллиард рублей тоже перебор")])
    submit = SubmitField("Submit")


class RegistrationTempForm(FlaskForm):
    login = StringField("Login ", [
        wtforms.validators.Length(1, 20, "Логин должен быть длиной от 1 до 20 символов"),
        wtforms.validators.Regexp("[a-zA-Z0-9_]+", message="Логин должен состоять из латинских букв и цифр")
    ])
    type_user = SelectField(choices=['owner', 'client'])
    psw = PasswordField("Password ", [InputRequired(), EqualTo('confirm',
                                                               message='Passwords must match')])
    psw2 = PasswordField("Repeat password ")
    submit = SubmitField("Submit")


class ReportForm(FlaskForm):
    status = SelectField(choices=['done', 'unfinished'])
    report_content = TextAreaField("Content ", [
        wtforms.validators.Length(0, 2000, "Ваш отзыв должен не превышать 20000 символов")
    ])
    submit = SubmitField("Submit")


class RateForm(FlaskForm):
    mark = SelectField(choices=[1, 2, 3, 4, 5])
    feedback_message = TextAreaField("Write down some comments", [
        wtforms.validators.Length(0,2000, "Ваш отзыв должен не превышать 20000 символов")
    ])
    submit = SubmitField("Submit")
