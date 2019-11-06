class Stemmer:
    def __init__(self):
        self.remove_end = ["ات", "ان", "ترین", "تر", "یی", "ها", "ٔ", " ‌"]
        self.replace_end = {
            "ۀ": "ه"
        }

    def _endswith(self, word):
        for end in self.remove_end:
            if word.endswith(end):
                word = word[:-len(end)]
        for end in self.replace_end:
            if word.endswith(end):
                word = word[:-len(end)] + self.replace_end[end]
        return word

    def stem(self, word):
        word = self._endswith(word)
        return word


if __name__ == '__main__':
    stemmer = Stemmer()
    print(stemmer.stem('سلامتترین'))
