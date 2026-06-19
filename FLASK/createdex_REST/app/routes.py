from flask import jsonify
from app import app
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