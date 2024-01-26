from flask import Flask, request, jsonify, json, session
import mysql.connector
from passlib.hash import bcrypt  # Import the bcrypt hashing library
from flask_cors import CORS
from werkzeug.utils import secure_filename


app = Flask(__name__)
CORS(app)


db = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",  
            database="ntuaflix",
            charset="utf8mb4",
            collation="utf8mb4_general_ci"
        )


@app.route('/admin/healthcheck', methods=['GET'])
def healthcheck():
    # Here you would add your logic to check database or API connectivity.
    # I'm using a mock response for demonstration purposes.

    # Check if database or API is connected (mock example)
    is_connected = True  # Replace this with actual connectivity check

    # Generate connection string (mock example)
    connection_string = "host=localhost dbname=mydb user=myuser password=mypass"  # Replace with real connection string

    # Prepare response based on connectivity
    if is_connected:
        response = {"status": "OK", "dataconnection": connection_string}
    else:
        response = {"status": "failed", "dataconnection": connection_string}

    return jsonify(response)

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)