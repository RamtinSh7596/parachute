import re
from tokenizer.stemmer import Stemmer
from tokenizer.matcher import Matcher
from tokenizer.normalizer import Normalizer


class Tokenizer:
    def __init__(self):
        self.stemmer = Stemmer()
        self.matcher = Matcher('./matches.json')
        self.normalizer = Normalizer()

    def tokenize(self, text):
        normal_text = self.normalizer.affix_spacing(text)
        tokens = re.split(' |-|\\?|\\.|\n|\\؟', normal_text)
        tokens = filter(lambda x: x != '', tokens)
        for token in tokens:
            token = self.stemmer.stem(token)
            token = self.matcher.check(token)
            yield token
