from flask import render_template, request, flash
from app import app, db
from app.forms import CalculatePaint
from app.models import calculation


@app.route("/")
def main():
    form = CalculatePaint()
    return render_template("index.html", form=form)


@app.route("/calculations")
def calculations():
    rows = calculation.query.all()
    return render_template("calculations.html", rows=rows)


@app.route("/calculate", methods=["POST"])
def calculate():
    form = CalculatePaint()

    num1 = request.form["num1"]
    num2 = request.form["num2"]

    result = int(num1) * int(num2)

    new_calculation = calculation(
        num1=int(num1),
        num2=int(num2),
        result=result
    )

    if form.validate_on_submit():
        db.session.add(new_calculation)
        db.session.commit()

        flash("Calculation added to database!")

    return render_template("index.html", form=form, result=result)