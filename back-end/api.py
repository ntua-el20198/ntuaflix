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
    "password": "2255",  
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
    if request.method == 'GET':
        # Check if the database connection is successful
        is_connected = db.is_connected() if db else False

        if is_connected:
            response = {"status": "OK", "dataconnection": db}, 200
        else:
            response = {"status": "Failed", "dataconnection": db}, 204

        return jsonify(response)
    else:
        return jsonify({"error": "Method Not Allowed"}), 404


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
    
    return jsonify({"error" : "Internal server error"}), 500

@app.route('/title/<int:titleID>', methods=['GET'])
def title(titleID):
    if request.method == 'GET':
        cursor = db.cursor()

        query_basics = "SELECT tconst, titletype, originalTitle, img_url_asset, startYear, endYear, genres FROM title_basics WHERE tconst = %s"
        cursor.execute(query_basics,(titleID,))

        title_data = cursor.fetchone()

        if title_data:
            try:
                column_names = ["titleID", "type", "originalTitle", "titlePoster", "startYear", "endYear", "genres"]
                title = dict(zip(column_names, title_data))
                title['genres'] = title['genres'].split(',')
                title['startYear'] = str(title['startYear'])
                title['titleID'] = str(title['titleID'])

                query_akas = "SELECT title, region FROM title_akas WHERE titleID = %s"
                cursor.execute(query_akas, (titleID,))
                title_akas = cursor.fetchall()

                if title_akas:
                     title['titleAkas'] = [{'titleAkas': akas[0], 'regionAbbrev': akas[1]} for akas in title_akas]
                
                query_principals = "SELECT tp.name_basicsnconst, nb.Primaryname, tp.category FROM title_principals tp INNER JOIN name_basics nb ON tp.name_basicsnconst = nb.nconst WHERE tp.tconst = %s"
                cursor.execute(query_principals, (titleID,))
                title_principals = cursor.fetchall()
                

                if title_principals:
                    title['principals'] = [{'nameID': str(principal[0]), 'name': principal[1], 'category': principal[2]} for principal in title_principals]

                query_rating = "SELECT averageRating, numVotes FROM title_ratings WHERE tconst = %s"
                cursor.execute(query_rating,(titleID,))
                title_rating = cursor.fetchone()

                if title_rating:
                    title['rating'] = {'avRating': str(title_rating[0]), 'numVotes': str(title_rating[1])}

                return jsonify(title), 200
            except Exception as e:
                print("Error in query_akas execution:", str(e))
                return jsonify({"error": "Internal server error"}), 500

        else:
            return jsonify({"error": "Title not found"}), 204
    
    else:
        return jsonify({"error": "Method Not Allowed"}), 404
    
    return jsonify({"error" : "Internal server error"}), 500


@app.route('/name/<int:nameID>', methods=['GET'])
def name(nameID):
    if request.method == 'GET':
        cursor = db.cursor()

        query_basics = "SELECT nconst, primaryName, img_url_asset, birthYear, deathYear, primaryProfession FROM name_basics WHERE nconst = %s"
        cursor.execute(query_basics,(nameID,))

        name_data = cursor.fetchone()

        if name_data:
            try:
                column_names = ["nameID", "name", "namePoster", "birthYr", "deathYr", "profession"]
                name = dict(zip(column_names, name_data))
                
                query_principals = "SELECT  tp.tconst, tp.category FROM title_principals tp INNER JOIN name_basics nb ON tp.name_basicsnconst = nb.nconst WHERE tp.name_basicsnconst = %s"
                cursor.execute(query_principals, (nameID,))
                name_principals = cursor.fetchall()

                if name_principals:
                    name['nameTitles'] = list(name_principals)

                return jsonify(name), 200
            except Exception as e:
                print("Error in query_akas execution:", str(e))
                return jsonify({"error": "Internal server error"}), 500

        else:
            return jsonify({"error": "Title not found"}), 204
    
    else:
        return jsonify({"error": "Method Not Allowed"}), 404
    
    return jsonify({"error" : "Internal server error"}), 500

@app.route('/searchTitle', methods=['GET'])
def searchTitle():
    if request.method == 'GET':
        cursor = db.cursor()

        data = request.get_json()  # take the data from the body
        titlePart = data.get('titlePart')

        if titlePart:
            query_basics = "SELECT tconst, titletype, originalTitle, img_url_asset, startYear, endYear, genres FROM title_basics WHERE originalTitle LIKE %s"
            cursor.execute(query_basics, (f"%{titlePart}%",))
            titles = cursor.fetchall()

            title_list = []

            for title_info in titles:
                title_dict = {
                    'titleID': str(title_info[0]),
                    'type': title_info[1],
                    'originalTitle': title_info[2],
                    'titlePoster': title_info[3],
                    'startYear': str(title_info[4]),
                    'endYear': str(title_info[5]),
                    'genres': title_info[6].split(',') if title_info[6] else []
                }

                # Fetch title_akas for each title
                query_akas = "SELECT title, region FROM title_akas WHERE titleID = %s"
                cursor.execute(query_akas, (title_info[0],))
                title_akas = cursor.fetchall()

                if title_akas:
                    title_dict['titleAkas'] = [{'titleAkas': akas[0], 'regionAbbrev': akas[1]} for akas in title_akas]

                # Fetch title_principals for each title
                query_principals = "SELECT tp.name_basicsnconst, nb.Primaryname, tp.category FROM title_principals tp INNER JOIN name_basics nb ON tp.name_basicsnconst = nb.nconst WHERE tp.tconst = %s"
                cursor.execute(query_principals, (title_info[0],))
                title_principals = cursor.fetchall()

                if title_principals:
                    title_dict['principals'] = [{'nameID': str(principal[0]), 'name': principal[1], 'category': principal[2]} for principal in title_principals]

                # Fetch title_rating for each title
                query_rating = "SELECT averageRating, numVotes FROM title_ratings WHERE tconst = %s"
                cursor.execute(query_rating, (title_info[0],))
                title_rating = cursor.fetchone()

                if title_rating:
                    title_dict['rating'] = {'avRating': str(title_rating[0]), 'numVotes': str(title_rating[1])}

                title_list.append(title_dict)

            return jsonify(title_list), 200

    # Return an empty list if no titles are found or if titlePart is not provided
    return jsonify({'titles': []}), 200



if __name__ == "__main__":
    app.run(debug=True)
