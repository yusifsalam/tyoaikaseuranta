from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')

    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=3, max=20)])
    username = StringField('Username', [validators.Length(min=3, max=20)])
    password = PasswordField('Password', [validators.Length(min=5), validators.DataRequired(),
                                          validators.EqualTo('confirm_password', message='Passwords do not match!')])
    confirm_password = PasswordField('Confirm Password')

    class Meta:
        csrf = False
