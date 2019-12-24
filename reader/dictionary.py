class Dictionary:
    def __init__(self):
        self.dict = {}
        self.tokens = []

    def add(self, token, doc, position):
        if token not in self.dict:
            self.dict[token] = {doc: [position]}
            self.tokens.append(token)
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


if __name__ == '__main__':
    dictionary = Dictionary()
    dictionary.add('test', 1, 2)
    dictionary.add('test', 2, 3)
    dictionary.add('test', 1, 10)
    print(dictionary.get('test'))
    print(dictionary.get('test1'))
