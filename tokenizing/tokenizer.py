import re
from tokenizing.stemmer import Stemmer
from tokenizing.matcher import Matcher
from tokenizing.normalizer import Normalizer


class Tokenizer:
    def __init__(self, matches_path, exceptions_path):
        self.stemmer = Stemmer(exceptions_path)
        self.matcher = Matcher(matches_path)
        self.normalizer = Normalizer()

    def tokenize(self, text):
        normal_text = self.normalizer.affix_spacing(text)
        tokens = re.split(' |-|\\?|\\.|\n|\\؟', normal_text)
        tokens = filter(lambda x: x != '', tokens)
        for token in tokens:
            token = self.stemmer.stem(token)
            token = self.matcher.check(token)
            yield token


if __name__ == '__main__':
    tokenizer = Tokenizer('../matches.json', '../exceptions.txt')
    print(tokenizer.tokenize("سلام طهران، می خواهیم تست کنیم!"))
