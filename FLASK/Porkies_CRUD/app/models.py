from datetime import datetime
from app import db


class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    vehicle = db.Column(db.String(100), nullable=False)

    orders = db.relationship("Order", backref="driver", lazy=True)

    def __repr__(self):
        return f"<Driver {self.name}>"


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    customer_name = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(50), nullable=False)
    customer_address = db.Column(db.String(200), nullable=False)

    order_details = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Pending")

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.id"), nullable=True)

    def __repr__(self):
        return f"<Order {self.id} - {self.customer_name}>"