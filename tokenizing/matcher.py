import json


class Matcher:
    def __init__(self, matches_file):
        with open(matches_file, 'r') as file:
            self.matches = json.load(file)

    def check(self, word):
        try:
            return self.matches[word]
        except KeyError:
            return word


if __name__ == '__main__':
    matcher = Matcher('../matches.json')
    print(matcher.check("طهران"))
    print(matcher.check("تست"))
