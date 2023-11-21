import os
from flask import Flask, redirect, flash, render_template, request, url_for, g
import mysql.connector
from forms import ApplicationForm, ClientBuyForm, CompanyBuyForm, FlatForm, LoginForm, RateForm, RegistrationForm, \
    RegistrationTempForm, ReportForm
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from UserLogin import UserLogin
from werkzeug.utils import secure_filename

SECRET_KEY = 'sekret'
DEBUG = True
DATABASE = '/tmp/agency.db'

UPLOAD_FOLDER = '/flaska/static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'agency.db')))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from flask_bootstrap import Bootstrap

login_manager = LoginManager(app)
bootstrap = Bootstrap(app)

login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"


def connect_db():
    conn = mysql.connector.connect(user='root',
                                   password='123QWEasdzxc',
                                   host='localhost',
                                   port='3306',
                                   database='agency')
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('ag_gen.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    with app.open_resource('ag_fill.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'agency.db'):
        g.link_db = connect_db()
    return g.link_db


dbase = None


@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link.db'):
        g.link_db.close()


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().from_db(user_id, dbase)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# Обработчик Домашней страницы
@app.route('/')
def home():
    return render_template('home.html', user=current_user, username=current_user)


# Обработчик страницы сделок для подтверждения
@app.route('/profile/deals/')
@login_required
def approve_deals():
    page_obj = dbase.get_unapplied_deals()
    print(page_obj)
    return render_template('approve_deals.html', page_obj=page_obj, user=current_user, )


# Обработчик страницы с объявлениями на продажу квартир
@app.route('/buy/')
def buy():
    page_obj = dbase.get_table('flat')
    print(page_obj)
    return render_template('buy.html', page_obj=page_obj, user=current_user, )


# Обработчик страницы с конкретным объявлением
@app.route('/buy/<int:flat_id>/')
def buy_page(flat_id):
    page_obj = dbase.get_flat_info(flat_id)[0]
    dbase.flat_view(flat_id)
    print(page_obj)
    return render_template('flat.html', page_obj=page_obj, user=current_user)


# Обработчик страницы с формой для аренды квартиры компанией
@app.route('/buy/<int:flat_id>/deal_company/', methods=["POST", "GET"])
def deal_company(flat_id):
    form = CompanyBuyForm()
    if request.method == "POST" and form.validate():
        try:
            res = dbase.add_company_deal(request.form['taxpayer_identification_number'],
                                         request.form['contact_information'],
                                         request.form['company_price'], flat_id)
            if not res:
                flash('Ошибка отправки', category='error')
            else:
                return redirect(url_for('rate', deal_id=res))
        except:
            flash('ошибка отправки, пожалуйста, перепроверьте введенные данные')
    return render_template('deal_company.html', form=form)


# Обработчик страницы с формой для покупки квартиры физическим лицом
@app.route('/buy/<int:flat_id>/deal_client/', methods=["POST", "GET"])
def deal_client(flat_id):
    form = ClientBuyForm()
    if form.validate_on_submit():
        try:
            res = dbase.add_client_deal(request.form['phone_number'], request.form['email'],
                                        request.form['type_of_deal'], request.form['client_price'], flat_id)
            if not res:
                flash('Ошибка отправки', category='error')
            else:
                return redirect(url_for('rate', deal_id=res))
        except:
            flash('ошибка отправки, пожалуйста, перепроверьте введенные данные')
    return render_template('deal_client.html', form=form)


# Обработчик страницы с формой для отзыва
@app.route('/rate/<int:deal_id>/', methods=["POST", "GET"])
def rate(deal_id):
    form = RateForm()
    if form.validate_on_submit():
        try:
            res = dbase.add_rate(deal_id, request.form['mark'], request.form['feedback_message'])
            if not res:
                flash('Ошибка отправки', category='error')
            else:
                return redirect(url_for('home'))
        except:
            flash('ошибка отправки, пожалуйста, перепроверьте введенные данные')
    return render_template('deal_client.html', form=form)


# Обработчик страницы с открытыми вакансиями
@app.route('/join/')
def join():
    page_obj = dbase.get_vacancy_and_position()
    print(page_obj)
    return render_template('join.html', page_obj=page_obj, user=current_user)


# Обработчик страницы с конкретной вакансией
@app.route('/join/<int:vacancy_id>/', methods=["POST", "GET"])
def join_form(vacancy_id):
    vacancy = dbase.get_vacancy(vacancy_id)
    form = ApplicationForm()
    if request.method == "POST" and form.validate():
        try:
            res = dbase.add_application(request.form['phone_number'], request.form['email'], request.form['letter'],
                                        vacancy[0])
            if not res:
                flash('Ошибка отправки', category='error')
            else:
                return redirect(url_for('home'))
        except:
            flash('ошибка отправки, пожалуйста, перепроверьте введенные данные')
    return render_template('application.html', form=form)


# Обработчик страницы с заявками на вакансии
@app.route('/profile/app_list/')
@login_required
def app_list():
    page_obj = dbase.get_app_pos()
    return render_template('app_list.html', page_obj=page_obj, user=current_user)


# Обработчик страницы с формой для продажи квартиры
@app.route('/sell/', methods=["POST", "GET"])
def sell():
    form = FlatForm()
    if request.method == "POST" and form.validate():
        try:
            res = dbase.add_flat(
                request.form['floor'], request.form['area'], request.form['price'],
                request.form['rooms'], request.form['phone_number'],
                request.form['street'], request.form['parking'], request.form['playground'],
                request.form['floors_count'], request.form['number'], request.form['birth_date'],
                request.form['distance_underground'], request.form['distance_bus_stop']
            )
            file = request.files['photo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                os.mkdir(app.config['UPLOAD_FOLDER'] + f'flat_{res}')
                file.save(os.path.join(app.config['UPLOAD_FOLDER'] + f'flat_{res}', 'image.png'))
                return redirect(url_for('home'))
            if not res:
                flash('Ошибка отправки', category='error')
            else:
                print(request.form.get('photo', False))
                return redirect(url_for('home'))
        except:
            flash('ошибка отправки, пожалуйста, перепроверьте введенные данные')
    return render_template('sell.html', form=form)


# Обработчик страницы с заявкой для входа в систему для сотрудника
@app.route("/login/", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if request.method == "POST" and form.validate():
        try:
            user = dbase.getUserByLogin(request.form['login'])
            print(request.form['pwd'])
            if user and check_password_hash(user[3], request.form['pwd']):
                rm = True if request.form.get('remainme') else False
                userlogin = UserLogin().create(user)
                login_user(userlogin, remember=rm)
                return redirect(url_for('profile'))

            flash("Неверная пара логин/пароль", "error")

        except:
            flash('ошибка отправки, пожалуйста, перепроверьте введенные данные')
    return render_template("login.html", title="Авторизация", form=form, user=current_user)


# Обработчик страницы с заявкой для выхода из системы для сотрудника
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('home'))


# Обработчик страницы для удаления отзыва на вакансию
@app.route('/profile/app_list/delete_application/<int:application_id>/')
@login_required
def delete_app(application_id):
    dbase.delete_application(application_id)
    flash("Вы удалили заявку", "success")
    return redirect(url_for('app_list'))


# Обработчик страницы для подтверждения сделки
@app.route('/profile/app_list/approve/<int:deal_id>/')
@login_required
def approve_deal(deal_id):
    dbase.approve_deal(deal_id)
    flash("you approved deal", "success")
    return redirect(url_for('add_rep', deal_id=deal_id))


# Обработчик страницы для написания отчета
@app.route('/profile/app_list/approve/<int:deal_id>/report/', methods=["POST", "GET"])
@login_required
def add_rep(deal_id):
    form = ReportForm()
    if request.method == "POST" and form.validate():
        try:
            res = dbase.add_report(request.form['report_content'], request.form['status'], deal_id,
                                   current_user.get_id())
            if res:
                return redirect(url_for('approve_deals'))
            else:
                flash("Ошибка при добавлении в БД", "error")
        except:
            flash('ошибка отправки, пожалуйста, перепроверьте введенные данные')
    return render_template("register.html", title="Report", form=form)


# Обработчик страницы для принятия нового сотрудника
@app.route('/profile/app_list/approve_application/<int:application_id>/', methods=["POST", "GET"])
@login_required
def add_emp(application_id):
    phone_number = dbase.get_number_and_pos_id(application_id)[0]
    position_id = dbase.get_number_and_pos_id(application_id)[1]
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        try:
            if request.form['psw'] == request.form['psw2']:
                hash_psw = generate_password_hash(request.form['psw'])
                res = dbase.register_employee(request.form['login'], phone_number, position_id, hash_psw)
                if res:
                    flash("Вы добавили работника, теперь он может зайти под своим логином и паролем", "success")
                    return redirect(url_for('app_list'))
                else:
                    flash("Ошибка при добавлении в БД", "error")
            else:
                flash("Введите пароль корректно", "error")
        except:
            flash('ошибка отправки, пожалуйста, перепроверьте введенные данные')
    return render_template("register.html", title="Регистрация", form=form)


# Обработчик для отображения профиля сотрудника
@app.route('/profile/')
@login_required
def profile():
    return render_template('profile.html')


if __name__ == "__main__":
    app.run(debug=True)
