
from flask import Flask, send_from_directory
# creates a Flask application, named app
app = Flask(__name__)


# a route where we will display a welcome message via an HTML template
@app.route("/")
def index():
    return send_from_directory('.', 'index.html')


@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('.', path)


# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
