import util
from game import get_words
from datetime import date
import schedule
import time
import json
from game import LANGUAGES
import random
import os
import string
import sys
LANGUAGES = sorted(list(LANGUAGES.values()))

def job(t):
    game = {
		'id': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)),
		'games': get_words(5),
		'languages': LANGUAGES,
	}

    util.write('var GAME = ' + json.dumps(game , indent=2), 'data/game.js')
    if 'push' in sys.argv:
        os.system('git add data/game.js')
        os.system('git commit -m "generating new game"')
        os.system('git push')

    print('done')

schedule.every().day.at("00:01").do(job,'It is 00:01')

job(0)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
