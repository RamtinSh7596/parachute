class Stemmer:
    def __init__(self, exception_path=None):
        self.remove_end = ["ان", "یی", "ٔ", " ‌", "هایت",
                           "هایش", "هایم", " یم", "ها", "ای", " یت", "ها ", "ترین", "تر", "ات", " یش", "ت", "م",
                           "جات", "ش"]
        self.replace_end = {
            "ۀ": "ه"
        }
        self.exceptions = []
        if exception_path is not None:
            with open(exception_path, 'r', encoding='utf-8') as f:
                self.exceptions = [line[:-1] for line in f.readlines()]

    def stem(self, word):
        last = None
        while word not in self.exceptions and last != word:
            last = word
            for end in self.remove_end:
                if word.endswith(end):
                    last = word
                    word = word[:-len(end)]
                    break
        for end in self.replace_end:
            if word.endswith(end):
                word = word[:-len(end)] + self.replace_end[end]
        return word


if __name__ == '__main__':
    stemmer = Stemmer('../exceptions.txt')
    print(stemmer.stem('اتمام'))
