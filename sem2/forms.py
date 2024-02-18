from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, IntegerField, \
    EmailField
from wtforms.validators import DataRequired, Email


class UploadImageForm(FlaskForm):
    photo = FileField("Photo", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class GetLengthForm(FlaskForm):
    text = TextAreaField("Input text")
    submit = SubmitField('Submit')


class CalculateForm(FlaskForm):
    x = IntegerField("First number")
    y = IntegerField("Second number")
    operator = SelectField("Choose operation",
                           choices=[('+', 'сложение'), ('-', 'вычитание'), ('*', 'умножение'), ('/', 'деление')])
    submit = SubmitField('Submit')


class CheckAgeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age")
    submit = SubmitField('Submit')


class PowNumberForm(FlaskForm):
    number = IntegerField("Number")
    submit = SubmitField('Submit')


class NameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginWithEmailForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[Email()])
    submit = SubmitField('Submit')
