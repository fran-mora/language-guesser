import util
from game import get_word
from datetime import date
import schedule
import time
import json
from game import LANGUAGES
LANGUAGES = sorted(list(LANGUAGES.values()))
import random
import os
import string

def job(t):
	game = {
		'id': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)),
		'games': [],
		'languages': LANGUAGES,
	}

	for i in range(5):
		game['games'].append(get_word())

	util.write('var GAME = ' + json.dumps(game , indent=2), 'data/game.js')
	os.system('git add data/game.js')
	os.system('git commit -m "generating new game"')
	os.system('git push')

	print('done')

schedule.every().day.at("00:01").do(job,'It is 00:01')

if 'game.json' not in util.files('data'):
	job(0)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute