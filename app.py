
from flask import Flask, send_from_directory, request, render_template, session
from flask_session import Session
import util
from datetime import date
import random
import json
from game import LANGUAGES
LANGUAGES = sorted(list(LANGUAGES.values()))

today_game = util.readjson('data/game.json')

DOTS = ['🟢', '🟡', '🔴', '⚫'];


# creates a Flask application, named app
app = Flask(__name__)
app.secret_key = str(random.random())
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/static/<path:filename>')
def download_file(filename):
    return send_from_directory('/static/', filename)


@app.route('/guess',methods = ['POST'])
def guess():
    lang = request.form['language']
    games = session['games']
    true_lang = today_game['games'][len(games)-1][1]
    session['games'][-1].add(lang)
    if len(session['games'][-1]) == 3:
        return 'finished'
    return 'done'



@app.route('/next',methods = ['GET'])
def next():
    print(util.pink('next invoked'))
    games = session['games']
    true_lang = today_game['games'][len(games)-1][1]
    
    session['games'].append(set())
    return 'done'


@app.route('/get_status',methods = ['GET'])
def get_status():    
    return json.dumps({
        'guesses': list(session['games'][-1]),
        'progress': int((len(session['games'])-1) / len(today_game['games']) * 100),
        'score': ''.join([DOTS[len(x)-1] if today_game['games'][i][1] in x else DOTS[-1] for i,x in enumerate(session['games']) if len(x)])
    })


# a route where we will display a welcome message via an HTML template
@app.route("/")
def index():
    print(util.red(session))
    if not session.get('games') or session['date'] != today_game['date']:
        session['games'] = [set()]
        session['date'] = today_game['date']

    current_game = len(session['games'])-1
    progress = int((len(session['games'])-2) / len(today_game['games']) * 100)
    
    if current_game >= len(today_game['games']):
        return render_template('finished.html', progress=progress)

    word, language = today_game['games'][current_game]
    return render_template('index.html', word=word, language=language, languages=LANGUAGES,
        progress=progress)


# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)