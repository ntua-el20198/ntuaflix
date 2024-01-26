from flask import Flask, request, jsonify, json, session
import mysql.connector
from passlib.hash import bcrypt  # Import the bcrypt hashing library
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Database configuration
db_config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",  
    "database": "ntuaflix",
    "charset": "utf8mb4",
    "collation": "utf8mb4_general_ci"
}

# Connect to the database
db = mysql.connector.connect(**db_config)

@app.route('/admin/healthcheck', methods=['GET'])
def healthcheck():
    # Here you would add your logic to check database or API connectivity.
    # I'm using a mock response for demonstration purposes.

    # Check if database or API is connected (mock example)
    is_connected = True

    if is_connected:
        response = {"status": "OK", "dataconnection": db}
    else:
        response = {"status": "failed", "dataconnection": db}

    return jsonify(response)