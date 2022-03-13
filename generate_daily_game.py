import util
from game import get_word
from datetime import date
import schedule
import time


def job(t):
	game = {
	'date': str(date.today()),
	'games': [],
	}

	for i in range(5):
		game['games'].append(get_word())

	util.writejson(game, 'data/game.json')


schedule.every().day.at("00:01").do(job,'It is 00:01')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute