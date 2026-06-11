from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CalculatePaint(FlaskForm):
    num1 = StringField("First Number: ", validators=[DataRequired()])
    num2 = StringField("Second Number: ", validators=[DataRequired()])
    submit = SubmitField("Calculate + Add to DB")