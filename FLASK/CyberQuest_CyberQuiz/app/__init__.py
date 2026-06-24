from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "cyberquest-secret-key"

from app import routes