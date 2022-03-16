import util
import json
import random
import re
from collections import defaultdict
from tqdm import tqdm

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
 'zh_cn': 'Mandarin',
}


SYMBOLIC_LANGUAGES = {'zh_cn', 'ja', 'km', 'he', 'th', 'ar', 'ko'}
def extract_words(text, lang='en'):
    if lang in SYMBOLIC_LANGUAGES:
        text = re.sub(r"[a-zA-Z]", ' ', text)
    words = set(re.sub(r"[,.;\-:'\"@#”?!（）《》&？$()0-9]+\ *", " ", text.lower()).split())
    words = {word for word in words if len(word) > 1}
    if lang not in SYMBOLIC_LANGUAGES:
        words = {word for word in words if len(word) > 3}
    return words
    
def get_words(number):
    langs = list(LANGUAGES.keys())
    random.shuffle(langs)
    langs = langs[:number]
    return [
        (random.choice(list(UNIQUE_VOCAB[lang])), LANGUAGES[lang]) for lang in langs
    ]

data = [json.loads(line) for line in util.readlines('data/mkqa.jsonl')]
for x in data:
	del x['queries']['zh_hk']
	del x['queries']['zh_tw']


VOCABS = defaultdict(set)
for x in tqdm(data):
    for lang, query in x['queries'].items():
        VOCABS[lang] |= extract_words(query, lang)
    
UNIQUE_VOCAB = {}
for lang, vocab in VOCABS.items():
    other = set()
    for lang2, vocab2 in VOCABS.items():
        if lang != lang2:
            other |= vocab2
    UNIQUE_VOCAB[lang] = vocab-other
    


# def get_word():
# 	while True:
# 		questions = random.choice(data)['queries']
# 		languages = list(questions.keys())
# 		language = random.choice(languages)
# 		question = questions[language]
# 		other_words = {word for lang in questions if lang != language for word in get_words(questions[lang])}
# 		words = [word for word in get_words(question) if word not in other_words]
# 		if not words:
# 			continue
# 		word = random.choice(words)
# 		return word, LANGUAGES[language]