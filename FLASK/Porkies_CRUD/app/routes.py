from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import OrderForm
from app.models import Order, Driver


def get_driver_choices():
    drivers = Driver.query.order_by(Driver.name).all()

    choices = [(0, "Unassigned")]
    choices += [(driver.id, driver.name) for driver in drivers]

    return choices


@app.route("/")
def index():
    total_orders = Order.query.count()
    pending_orders = Order.query.filter_by(status="Pending").count()
    delivered_orders = Order.query.filter_by(status="Delivered").count()

    return render_template(
        "index.html",
        total_orders=total_orders,
        pending_orders=pending_orders,
        delivered_orders=delivered_orders,
    )


@app.route("/orders")
def orders():
    all_orders = Order.query.order_by(Order.created_at.desc()).all()

    return render_template(
        "orders.html",
        orders=all_orders,
    )


@app.route("/orders/new", methods=["GET", "POST"])
def new_order():
    form = OrderForm()
    form.driver_id.choices = get_driver_choices()

    if form.validate_on_submit():
        driver_id = form.driver_id.data

        if driver_id == 0:
            driver_id = None

        order = Order(
            customer_name=form.customer_name.data,
            customer_phone=form.customer_phone.data,
            customer_address=form.customer_address.data,
            order_details=form.order_details.data,
            status=form.status.data,
            driver_id=driver_id,
        )

        db.session.add(order)
        db.session.commit()

        flash("Order created successfully.")
        return redirect(url_for("orders"))

    return render_template("neworder.html", form=form)


@app.route("/orders/<int:order_id>/edit", methods=["GET", "POST"])
def edit_order(order_id):
    order = Order.query.get_or_404(order_id)

    form = OrderForm(obj=order)
    form.driver_id.choices = get_driver_choices()

    if request.method == "GET":
        form.driver_id.data = order.driver_id or 0

    if form.validate_on_submit():
        driver_id = form.driver_id.data

        if driver_id == 0:
            driver_id = None

        order.customer_name = form.customer_name.data
        order.customer_phone = form.customer_phone.data
        order.customer_address = form.customer_address.data
        order.order_details = form.order_details.data
        order.status = form.status.data
        order.driver_id = driver_id

        db.session.commit()

        flash("Order updated successfully.")
        return redirect(url_for("orders"))

    return render_template("editorder.html", form=form, order=order)

@app.route("/orders/<int:order_id>/delete", methods=["POST"])
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)

    db.session.delete(order)
    db.session.commit()

    flash("Order deleted successfully.")
    return redirect(url_for("orders"))