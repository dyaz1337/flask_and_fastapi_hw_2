from functools import wraps

from flask import Flask, render_template, request, flash, redirect, url_for, make_response
from werkzeug.utils import secure_filename
from forms import UploadImageForm, LoginForm, GetLengthForm, CalculateForm, CheckAgeForm, PowNumberForm, NameForm, \
    LoginWithEmailForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = b'8fda4c95f8ced93390919e911abb6b9dcd317ac21a6662e23748d47345e1cb72'
app.config['UPLOAD_FOLDER'] = './upload'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


def result(message):
    return render_template('result.html', message=message)


# Создать страницу, на которой будет кнопка "Нажми меня",
# при нажатии на которую будет переход на другую страницу с приветствием пользователя по имени.
@app.route('/task1/')
@app.route('/task1/index')
def task1_index():
    return render_template('task1/index.html', title='task1')


@app.route('/task1/welcome')
def task1_welcome(name='John'):
    if x := request.args.get('name'):
        name = x
    return render_template('task1/welcome.html', title='task1', name=name)


# Создать страницу, на которой будет изображение и ссылкана другую страницу,
# на которой будет отображаться форма для загрузки изображений.
@app.route('/task2/')
@app.route('/task2/index')
def task2_index():
    return render_template('task2/index.html', title='task2')


@app.route('/task2/upload', methods=['GET', 'POST'])
def task2_upload_img():
    form = UploadImageForm()
    if form.validate_on_submit():
        image = form.photo.data  # request.files.get('photo')
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename)))
        flash("Photo uploaded", 'success')
    return render_template('task2/upload_img.html', title='task2', form=form)


# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля
# и переход на страницу приветствия пользователя или страницу с ошибкой.
users = {'admin': '1111', 'user': '2222'}


@app.route('/task3/', methods=['GET', 'POST'])
@app.route('/task3/login', methods=['GET', 'POST'])
def task3_login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.login.data  # request.form.get('login')
        password = form.password.data  # request.form.get('password')
        if users.get(name) == password:
            return task1_welcome(name)
        else:
            flash("Login and Password doesn't match!", 'danger')
    return render_template('task3/login.html', form=form, title='task3')


# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.
@app.route('/task4/', methods=['GET', 'POST'])
def task_4_get_length():
    form = GetLengthForm()
    if form.validate_on_submit():
        text = form.text.data  # request.form.get('text')
        return result(str(len(text.split())))
    return render_template('task4/index.html', form=form, title='task4')


# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции
# (сложение, вычитание, умножение или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление результата выбранной операции
# и переход на страницу с результатом.
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y else "Нельзя делить на 0"
}


@app.route('/task5/', methods=['GET', 'POST'])
def task5_calculate():
    form = CalculateForm()
    if form.validate_on_submit():
        x = form.x.data  # int(request.form.get('x'))
        y = form.y.data  # int(request.form.get('y'))
        operator = form.operator.data  # request.form.get('operator')
        return result(str(operations[operator](x, y)))
    return render_template('task5/index.html', form=form, title='task5')


# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка возраста
# и переход на страницу с результатом или на страницу с ошибкой в случае некорректного возраста.
@app.route('/task6/', methods=['GET', 'POST'])
def task6_check_age():
    form = CheckAgeForm()
    if form.validate_on_submit():
        name = form.name.data  # request.form.get('name')
        age = form.age.data  # int(request.form.get('age'))
        if age < 18:
            return result(message=f"{name}, Вам еще рано посещать такие сайты")
        return task1_welcome(name)
    return render_template('task6/index.html', form=form, title='task6')


# Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с результатом,
# где будет выведено введенное число и его квадрат.
@app.route('/task7/', methods=['GET', 'POST'])
def task7_check_age():
    form = PowNumberForm()
    if form.validate_on_submit():
        number = form.number.data  # int(request.form.get('number'))
        return result(f"{number} - pow(number) = {number ** 2}")
    return render_template('task7/index.html', form=form, title='task7')


# Создать страницу, на которой будет форма для ввода имении кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением,
# где будет выведено "Привет, {имя}!".
@app.route('/task8/', methods=['GET', 'POST'])
def task8_check_age():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data  # request.form.get('name')
        flash(f"Привет, {name}!", "success")
        return task1_welcome(name)
    return render_template('task8/index.html', form=form, title='task8')


# Создать страницу, на которой будет форма для ввода имени и электронной почты
# При отправке которой будет создан cookie файл с данными пользователя
# Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными пользователя
# и произведено перенаправление на страницу ввода имени и электронной почты.
def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if not request.cookies.get('name'):
            flash("Login required!", 'warning')
            return redirect(url_for('task9_login'))
        return f(*args, **kwargs)

    return inner


@app.route('/task9/login', methods=['GET', 'POST'])
def task9_login():
    form = LoginWithEmailForm()
    if form.validate_on_submit():
        name = form.name.data  # request.form.get('name')
        email = form.email.data  # request.form.get('email')
        response = make_response(redirect(url_for('task9_welcome')))
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        return response
    return render_template('task9/login.html', form=form, title='task9')


@app.route('/task9/', methods=['GET', 'POST'])
@login_required
def task9_welcome():
    name = request.cookies.get('name')
    email = request.cookies.get('email')
    if request.method == 'POST':
        resp = make_response(redirect(url_for('task9_login')))
        resp.delete_cookie('name')
        resp.delete_cookie('email')
        return resp
    return render_template('task9/index.html', name=name, email=email, title='task9')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
