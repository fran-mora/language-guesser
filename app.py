
from flask import Flask, session, send_from_directory, request
from flask import render_template
import util
import random
from game import get_word, LANGUAGES
LANGUAGES = sorted(list(LANGUAGES.values()))

# creates a Flask application, named app
app = Flask(__name__)
app.secret_key = str(random.random())


@app.route('/static/<path:filename>')
def download_file(filename):
    return send_from_directory('/static/', filename)


# a route where we will display a welcome message via an HTML template
@app.route("/")
def index():
    word, language = get_word()
    return render_template('index.html', word=word, language=language, languages=LANGUAGES)


# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)