from flaskr import create_app  # Importing the create_app function from the flaskr module

app = create_app()  # Creating a Flask application using the create_app function

if __name__ == "__main__":  # Checking if this file is being run directly
    app.run(debug=True)  # Starting the Flask application in debug mode for easier development
