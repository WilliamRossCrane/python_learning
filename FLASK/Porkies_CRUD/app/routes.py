from flask import render_template
from app import app
from app.models import Order


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