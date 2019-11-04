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
        # TODO remove!!!
        while True:
            if '' in tokens:
                tokens.remove('')
                break
        for token in tokens:
            print(token)
            token = self.stemmer.stem(token)
            token = self.matcher.matches(token)
            yield token
