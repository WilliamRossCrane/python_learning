from flask import jsonify, request
from app import app, db
from app.models import Creature


@app.route("/")
def index():
    return jsonify({
        "message": "Welcome to the CreateDex REST API",
        "description": "A beginner-friendly Flask API for managing fictional creatures.",
        "endpoints": {
            "health": "/api/health",
            "creatures": "/api/creatures"
        }
    })


@app.route("/api/health")
def health_check():
    return jsonify({
        "status": "ok",
        "message": "CreateDex API is running."
    })


@app.route("/api/creatures", methods=["GET"])
def get_creatures():
    creatures = Creature.query.order_by(Creature.id).all()

    return jsonify({
        "count": len(creatures),
        "creatures": [creature.to_dict() for creature in creatures]
    })


@app.route("/api/creatures", methods=["POST"])
def create_creature():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No JSON data provided."
        }), 400

    required_fields = ["name", "element", "level", "rarity"]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Missing required field: {field}"
            }), 400

    creature = Creature(
        name=data["name"],
        element=data["element"],
        level=data["level"],
        rarity=data["rarity"],
    )

    db.session.add(creature)
    db.session.commit()

    return jsonify({
        "message": "Creature created successfully.",
        "creature": creature.to_dict()
    }), 201