from flask import jsonify
from app import app


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