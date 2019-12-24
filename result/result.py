class Result:
    def __init__(self, doc, similarity):
        self.doc = doc
        self.similarity = similarity

    def __lt__(self, other):
        return other.similarity > self.similarity

    def __gt__(self, other):
        return other.similarity < self.similarity

    def __eq__(self, other):
        return other.similarity == self.similarity
