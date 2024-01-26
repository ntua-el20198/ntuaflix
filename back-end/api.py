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

try:
    db = mysql.connector.connect(**db_config)
except mysql.connector.Error as err:
    db = None
    print("Database connection failed:", err)


@app.route('/admin/healthcheck', methods=['GET'])
def healthcheck():
    # Check if the database connection is successful
    is_connected = db.is_connected() if db else False

    if is_connected:
        response = {"status": "OK", "dataconnection": "Connected"}
    else:
        response = {"status": "Failed", "dataconnection": "Not Connected"}

    return jsonify(response)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':

        try:
            # Extract username and password from form data
            username = request.form.get('username')
            password = request.form.get('password')

            if username is None or password is None:
                return jsonify({"error": "Request that doesn't return data"}), 204
            else:
                cursor = db.cursor()
                # Execute a query to check if the username and password exist in the same row
                query = "SELECT * FROM users WHERE Username = %s AND password = %s"
                cursor.execute(query, (username, password))

                # Fetch the result
                result = cursor.fetchone()

                if result:
                    return jsonify({"token": result }), 200
                else:
                    return jsonify({"error": "Not authorised"}), 401

        except Exception as e:
            # Log the exception for debugging
            print(str(e))
            # Internal server error
            return jsonify({"error": "Internal server error"}), 500
    else:
        return jsonify({"error": "Not Available"}), 404
        

if __name__ == "__main__":
    app.run(debug=True)