from typing import List
from functools import lru_cache
import nltk
import pymorphy2
import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download('brown')
corpus = nltk.corpus.brown

words = corpus.words()

morph = pymorphy2.MorphAnalyzer()

# Normalize texts
print(morph.parse('собаки')[0].normal_form)


# Saves repeating words
@lru_cache(maxsize=len(set(words)))
def normalize(word: str, morph: pymorphy2.MorphAnalyzer):
    return morph.parse(word)[0].normal_form


def normalize_corpus(words: List[str], morph: pymorphy2.MorphAnalyzer):
    return [normalize(word, morph) for word in words]


print(normalize_corpus(words, morph))
