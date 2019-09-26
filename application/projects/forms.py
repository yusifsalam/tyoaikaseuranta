from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField


class ProjectForm(FlaskForm):
    name = StringField("Project name", [validators.Length(min=2)])

    class Meta:
        csrf = False


class AddUser(FlaskForm):
    name = SelectField("User's name", coerce=int, validators=[validators.InputRequired()])

    class Meta:
        csrf = False
