from flask import Flask

# Create an instance of the Flask web application
app = Flask(__name__)

# Define a "route" - a URL our app will respond to
@app.route('/')
def hello():
    # Return this text when someone visits the main URL ("/")
    return "Hello, DevOps World!"

# This 'if' block makes the app run when you execute 'python app.py'
if __name__ == '__main__':
    # Run the app on host 0.0.0.0 (makes it accessible) and port 5000
    app.run(host='0.0.0.0', port=5000)
