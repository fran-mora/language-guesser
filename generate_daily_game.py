import util
from game import get_word
from datetime import date
import schedule
import time
import json
from game import LANGUAGES
LANGUAGES = sorted(list(LANGUAGES.values()))


def job(t):
	game = {
		'date': str(date.today()),
		'games': [],
		'languages': LANGUAGES,
	}


	for i in range(5):
		game['games'].append(get_word())

	util.write('var GAME = ' + json.dumps(game , indent=2), 'data/game.js')
	print('done')

schedule.every().day.at("00:01").do(job,'It is 00:01')

if 'game.json' not in util.files('data'):
	job(0)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute