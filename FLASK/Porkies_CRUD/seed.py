from app import app, db
from app.models import Driver


drivers = [
    {"name": "Will", "vehicle": "Delivery Van"},
    {"name": "Dan", "vehicle": "Ute"},
    {"name": "Sarah", "vehicle": "Scooter"},
]


with app.app_context():
    for driver_data in drivers:
        existing_driver = Driver.query.filter_by(name=driver_data["name"]).first()

        if existing_driver is None:
            driver = Driver(
                name=driver_data["name"],
                vehicle=driver_data["vehicle"],
            )

            db.session.add(driver)

    db.session.commit()

    print("Driver seed data added successfully.")