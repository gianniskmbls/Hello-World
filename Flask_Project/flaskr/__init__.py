import os  # Importing the os module for operating system interactions
from flask import Flask, request, jsonify, render_template  # Importing essential Flask components
from flask_mysqldb import MySQL  # Importing MySQL integration for Flask

# Function to create and configure the Flask application
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True) # Creating a Flask app instance with the name of the current module

    # Default configuration for the app, including MySQL database settings
    app.config.from_mapping(
        SECRET_KEY='dev',                # Secret key for session management
        MYSQL_HOST='localhost',          # MySQL server host
        MYSQL_USER='root',           # MySQL user
        MYSQL_PASSWORD='admin123',       # MySQL user's password
        MYSQL_DB='bankdb',             # MySQL database name
    )

    # If a test configuration is provided, we load it; otherwise, we try to load configuration from config.py
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Ensuring the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initializing MySQL extension with the app
    mysql = MySQL(app)

    # Route for the homepage, which renders an HTML template called 'index.html'
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # Route to add a new bank, accepts POST requests with JSON data
    @app.route('/banks', methods=['POST'])
    def add_bank():
        data = request.json  # Getting the JSON data from the request
        cursor = mysql.connection.cursor()  # Getting a cursor to interact with the database
        cursor.execute(
            'INSERT INTO banks (name, location) VALUES (%s, %s)',  # SQL query to insert new bank data
            (data['name'], data['location'])  # Values to insert from the request data
        )
        mysql.connection.commit()  # Committing the transaction to the database
        cursor.close()  # Closing cursor
        return jsonify({'message': 'Bank added successfully!'}), 201  # Return a success message with HTTP status 201

    # Route to get a list of all banks, accepts GET requests
    @app.route('/banks', methods=['GET'])
    def get_banks():
        cursor = mysql.connection.cursor()  # Getting a cursor to interact with the database
        cursor.execute('SELECT * FROM banks')  # SQL query to select all banks
        banks = cursor.fetchall()  # Fetching all the results from the query
        cursor.close()  # Closing cursor
        return jsonify(banks), 200  # Returning the list of banks as JSON with HTTP status 200

    # Route to update a bank's information, accepts PUT requests with JSON data
    @app.route('/banks/<int:bank_id>', methods=['PUT'])
    def update_bank(bank_id):
        data = request.json  # Getting the JSON data from the request
        cursor = mysql.connection.cursor()  # Getting a cursor to interact with the database
        cursor.execute(
            'UPDATE banks SET name = %s, location = %s WHERE id = %s',  # SQL query to update bank data
            (data['name'], data['location'], bank_id)  # Values to update from the request data and the bank ID
        )
        mysql.connection.commit()  # Committing transaction to the database
        cursor.close()  # Closing cursor
        return jsonify({'message': 'Bank updated successfully!'}), 200  # Return a success message with HTTP status 200

    # Route to delete a bank, accepts DELETE requests
    @app.route('/banks/<int:bank_id>', methods=['DELETE'])
    def delete_bank(bank_id):
        cursor = mysql.connection.cursor()  # Getting a cursor to interact with the database
        cursor.execute('DELETE FROM banks WHERE id = %s', (bank_id,))  # SQL query to delete the bank by ID
        mysql.connection.commit()  # Committing the transaction to the database
        cursor.close()  # Closing cursor
        return jsonify({'message': 'Bank deleted successfully!'}), 204  # Return a success message with HTTP status 204

    return app  # Return the configured Flask app instance
