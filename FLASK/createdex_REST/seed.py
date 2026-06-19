from app import app, db
from app.models import Creature


creatures = [
    {
        "name": "Flameling",
        "element": "Fire",
        "level": 12,
        "rarity": "Rare",
    },
    {
        "name": "Aquabub",
        "element": "Water",
        "level": 8,
        "rarity": "Common",
    },
    {
        "name": "Thornox",
        "element": "Earth",
        "level": 18,
        "rarity": "Epic",
    },
    {
        "name": "Voltwing",
        "element": "Electric",
        "level": 15,
        "rarity": "Rare",
    },
]


with app.app_context():
    for creature_data in creatures:
        existing_creature = Creature.query.filter_by(
            name=creature_data["name"]
        ).first()

        if existing_creature is None:
            creature = Creature(
                name=creature_data["name"],
                element=creature_data["element"],
                level=creature_data["level"],
                rarity=creature_data["rarity"],
            )

            db.session.add(creature)

    db.session.commit()

    print("Creature seed data added successfully.")