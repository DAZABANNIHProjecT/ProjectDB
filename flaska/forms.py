import wtforms.validators
from flask_wtf import FlaskForm
from wtforms import EmailField, FileField, MultipleFileField, SelectField, SelectMultipleField, StringField, \
    SubmitField, BooleanField, PasswordField, IntegerField, DateField, TelField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, InputRequired, EqualTo


class FlatForm(FlaskForm):
    floor = IntegerField("Этаж: ", [wtforms.validators.number_range(
        -2, 200, "В Бурдж Халифе всего 163 этажа, вы наверное, что то путаете"
    )])
    area = IntegerField("Площадь: ", [wtforms.validators.number_range(
        0, 1000000000, "Площадь квартиры не может быть отрицательным числом, или же миллиард кв. м тоже перебор"
    )])
    price = IntegerField("Цена: ", [wtforms.validators.number_range(
        0, 500000000000, "Цена квартиры не может быть отрицательным числом, или же 500 миллиард рублей тоже перебор"
    )])
    rooms = SelectField("Комнаты:", choices=[1, 2, 3, 4, 5])
    phone_number = StringField("Phone ", [wtforms.validators.Regexp(
        "[8][\\d]{10}", message="Введите телефонный номер с восьмерки"
    )])
    street = StringField("Введите улицу: ", [wtforms.validators.Length(
        0, 50, "Название улицы не должно преавшать 500 символов"
    )])
    parking = SelectField("Введите количество парковок: ", choices=[0, 1, 2, 3])
    playground = SelectField("Введите количество детских площадок: ", choices=[0, 1, 2, 3])
    floors_count = IntegerField("Введите количество этажей в доме: ", [wtforms.validators.number_range(
        -2, 200, "В Бурдж Халифе всего 163 этажа, вы наверное, что то путаете"
    )])
    number = StringField("ВВедите серию и номер паспорта: ", [wtforms.validators.Regexp(
        "[8][\\d]{10}", message="Введите телефонный номер с восьмерки"
    )])
    birth_date = DateField("Введите дату рождения: ")
    distance_underground = IntegerField("Введите расстояние до ближайщего метро: ", [wtforms.validators.number_range(
        0, 500000000000, "Расстояние не может быть отрицательным или таким большим"
    )])
    distance_bus_stop = IntegerField("Введите до расстояние до ближайщей автобусной остановки: ", [wtforms.validators.number_range(
        0, 500000000000, "Расстояние не может быть отрицательным или таким большим"
    )])
    photo = FileField("Загрузите фото квартиры")
    submit = SubmitField("Ввести")


class LoginForm(FlaskForm):
    login = StringField("Логин ", [
        wtforms.validators.Length(1, 20, "Логин должен быть длиной от 1 до 20 символов"),
        wtforms.validators.Regexp("[a-zA-Z0-9_]+", message="Логин должен состоять из латинских букв и цифр")
    ])
    pwd = PasswordField("Пароль ")
    submit = SubmitField("Подтвердить")


class ApplicationForm(FlaskForm):
    phone_number = StringField("Номер телефона ", [wtforms.validators.Regexp(
        "[8][\\d]{10}", message="Введите телефонный номер с восьмерки"
    )])
    email = EmailField("Электронная почта ")
    letter = TextAreaField("Дополнительная информация ", [wtforms.validators.Length(0, 2000, "Приложение не должно превышать 2000 символов")])
    submit = SubmitField("Подтвердить")


class RegistrationForm(FlaskForm):
    login = StringField("Логин ", [
        wtforms.validators.Length(1, 20, "Логин должен быть длиной от 1 до 20 символов"),
        wtforms.validators.Regexp("[a-zA-Z0-9_]+", message="Логин должен состоять из латинских букв и цифр")
    ])
    phone_number = StringField("Телефонный номер ", [wtforms.validators.Regexp("[8][\\d]{10}", message="Введите телефонный номер с восьмерки")])
    psw = PasswordField("Пароль ", [InputRequired(), EqualTo('подтвердить',
                                                               message='Пароли должны совпадать')])
    psw2 = PasswordField("Повторите пароль ")
    submit = SubmitField("Подтвердить")


class ClientBuyForm(FlaskForm):
    phone_number = StringField("Телефонный номер ", [wtforms.validators.Regexp("[8][\\d]{10}", message="Введите телефонный номер с восьмерки")])
    email = EmailField("Электронная почта ")
    type_of_deal = SelectMultipleField(choices=['Сдять', 'продать'])
    client_price = IntegerField('Введите вашу цену ', [wtforms.validators.number_range(0, 500000000000, "Цена квартиры не может быть отрицательным числом, или же 500 миллиард рублей тоже перебор")])
    submit = SubmitField("Подтвердить")


class CompanyBuyForm(FlaskForm):
    taxpayer_identification_number = IntegerField('Введите ваш ИНН '[wtforms.validators.Length(12, 12, "ИНН состоит из 12 цифр")])
    contact_information = EmailField("Введите электронную почту")
    company_price = IntegerField('Введите вашу цену ', [wtforms.validators.number_range(0, 500000000000, "Цена квартиры не может быть отрицательным числом, или же 500 миллиард рублей тоже перебор")])
    submit = SubmitField("Подтвердить")


class RegistrationTempForm(FlaskForm):
    login = StringField("Логин ", [
        wtforms.validators.Length(1, 20, "Логин должен быть длиной от 1 до 20 символов"),
        wtforms.validators.Regexp("[a-zA-Z0-9_]+", message="Логин должен состоять из латинских букв и цифр")
    ])
    type_user = SelectField(choices=['владелец', 'клиент'])
    psw = PasswordField("Пароль ", [InputRequired(), EqualTo('подтвердите',
                                                               message='Пароли должны совпадать')])
    psw2 = PasswordField("Повторите пароль ")
    submit = SubmitField("Подтвердить")


class ReportForm(FlaskForm):
    status = SelectField(choices=['Закрыта', 'Незакончена'])
    report_content = TextAreaField("Отчет по сделке ", [
        wtforms.validators.Length(0, 2000, "Ваш отзыв должен не превышать 20000 символов")
    ])
    submit = SubmitField("Подтвердить")


class RateForm(FlaskForm):
    mark = SelectField(choices=[1, 2, 3, 4, 5])
    feedback_message = TextAreaField("Напишите ваш отзыв", [
        wtforms.validators.Length(0,2000, "Ваш отзыв должен не превышать 20000 символов")
    ])
    submit = SubmitField("Подтвердить")
