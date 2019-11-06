import pandas as pd
from reader.dictionary import Dictionary
from reader.cleaner import Cleaner
from tokenizing import Tokenizer

cleaner = Cleaner()


class FileReader:
    def __init__(self, path, matches_path):
        sheet = pd.read_excel(path)
        self.articles = []
        self.dict = Dictionary()
        self.tokenizer = Tokenizer(matches_path)
        for article in sheet.itertuples(True, 'Article'):
            self.articles.append(article)
            text = cleaner.clean(article.content)
            tokens = self.tokenizer.tokenize(text)
            pos = 0
            for token in tokens:
                self.dict.add(token, article.Index, pos)
                pos += 1

    def get(self, keys):
        for key in keys:
            yield self.articles[key]

    def search(self, query):
        query_tokens = list(self.tokenizer.tokenize(query))
        res, res_not = [], []
        i = 0
        while i < len(query_tokens):
            token = query_tokens[i]
            if token == '!' and i != len(query_tokens):
                i += 1
                token = query_tokens[i]
                res_not.append(self.dict.get(token))
            else:
                res.append(self.dict.get(token))
            i += 1
        if len(res) == 0:
            return []
        final = set(res[0])
        for i in range(1, len(res)):
            final = final.intersection(set(res[i]))
        for n in res_not:
            final = final - set(n)
        return self.get(final)


if __name__ == '__main__':
    file_reader = FileReader('../data/IR-F19-Project01-Input.xlsx', '../matches.json')
    docs = file_reader.search("تست برای")
    for doc in docs:
        print(doc)
