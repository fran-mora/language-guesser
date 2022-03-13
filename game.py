import util
import json
import random
import re

LANGUAGES = {
 'ar': 'Arabic',
 'da': 'Danish',
 'de': 'German',
 'en': 'English',
 'es': 'Spanish',
 'fi': 'Finnish',
 'fr': 'French',
 'he': 'Hebrew',
 'hu': 'Hungarian',
 'it': 'Italian',
 'ja': 'Japanese',
 'km': 'Cambodian',
 'ko': 'Korean',
 'ms': 'Malay',
 'nl': 'Dutch',
 'no': 'Norwegian',
 'pl': 'Polish',
 'pt': 'Portuguese',
 'ru': 'Russian',
 'sv': 'Swedish',
 'th': 'Thai',
 'tr': 'Turkish',
 'vi': 'Vietnamese',
 'zh_cn': 'Chinese',
}

data = [json.loads(line) for line in util.readlines('data/mkqa.jsonl')]
for x in data:
	del x['queries']['zh_hk']
	del x['queries']['zh_tw']


def get_words(text):
	words = set(re.sub(r"[,.;\-:'\"@#?!&$]+\ *", " ", text.lower()).split())
	return {word for word in words if len(word) > 3}


def get_word():
	while True:
		questions = random.choice(data)['queries']
		languages = list(questions.keys())
		language = random.choice(languages)
		question = questions[language]
		other_words = {word for lang in questions if lang != language for word in get_words(questions[lang])}
		words = [word for word in get_words(question) if word not in other_words]
		if not words:
			continue
		word = random.choice(words)
		return word, LANGUAGES[language]