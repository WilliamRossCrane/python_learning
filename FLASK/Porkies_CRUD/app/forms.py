from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class OrderForm(FlaskForm):
    customer_name = StringField(
        "Customer Name",
        validators=[DataRequired(), Length(max=100)]
    )

    customer_phone = StringField(
        "Customer Phone",
        validators=[DataRequired(), Length(max=50)]
    )

    customer_address = StringField(
        "Customer Address",
        validators=[DataRequired(), Length(max=200)]
    )

    order_details = TextAreaField(
        "Order Details",
        validators=[DataRequired()]
    )

    status = SelectField(
        "Order Status",
        choices=[
            ("Pending", "Pending"),
            ("Preparing", "Preparing"),
            ("Out for Delivery", "Out for Delivery"),
            ("Delivered", "Delivered"),
            ("Cancelled", "Cancelled"),
        ],
        validators=[DataRequired()]
    )

    driver_id = SelectField(
        "Driver",
        coerce=int,
        validators=[Optional()]
    )

    submit = SubmitField("Save Order")