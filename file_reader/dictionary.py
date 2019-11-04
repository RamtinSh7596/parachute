from tokenizer import stemmer, matcher


class Dictionary:
    def __init__(self):
        self.dict = {}

    def add(self, token, doc, position):
        if token not in self.dict:
            self.dict[token] = {doc: [position]}
        else:
            if doc in self.dict[token]:
                self.dict[token][doc] += [position]
            else:
                self.dict[token].update({doc: [position]})

    def get(self, key):
        try:
            return self.dict[key]
        except KeyError:
            return {}

    def sort(self):
        for key in self.dict:
            self.dict[key].sort()

    def frequents(self, f):
        for key in self.dict:
            if len(self.dict[key]) > f:
                yield key

    def load(self):
        pass

    def save(self):
        pass
