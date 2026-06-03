import os
import time
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="../build", static_url_path="")

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

