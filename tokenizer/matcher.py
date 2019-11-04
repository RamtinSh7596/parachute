import json


class Matcher:
    def __init__(self, matches_file):
        with open(matches_file, 'r') as file:
            self.matches = json.load(file)

    def check(self, word):
        for match in self.matches:
            if word == match:
                return self.matches[match]
        return word


if __name__ == '__main__':
    matcher = Matcher('./matches.json')
    print(matcher.check("طهران"))
    print(matcher.check("تست"))
