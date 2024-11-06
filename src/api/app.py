# src/api/app.py
from flask import Flask
from flask_cors import CORS
from endpoints import data_blueprint

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests from React frontend
app.register_blueprint(data_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
