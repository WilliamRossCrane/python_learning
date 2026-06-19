from app import db


class Creature(db.Model):
    __tablename__ = "creatures"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    element = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    rarity = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "element": self.element,
            "level": self.level,
            "rarity": self.rarity,
        }

    def __repr__(self):
        return f"<Creature {self.name}>"