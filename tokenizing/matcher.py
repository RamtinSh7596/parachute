import json


class Matcher:
    def __init__(self, matches_file):
        with open(matches_file, 'r', encoding='utf-8') as file:
            self.matches = json.load(file)

    def check(self, word):
        try:
            return self.matches[word]
        except KeyError:
            return word


if __name__ == '__main__':
    matcher = Matcher('../matches.json')
    print(matcher.check("بخواهد"))
    print(matcher.check("گفتند"))
