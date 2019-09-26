from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField,validators


class TaskForm(FlaskForm):
    category = StringField("Task name", [validators.Length(min=2)])
    hours = DecimalField("Hours spent", [validators.NumberRange(min=1/60)])
    description = StringField("Task description", [validators.Length(min=5)])

    class Meta:
        csrf = False
