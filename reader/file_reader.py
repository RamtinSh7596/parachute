import pandas as pd
from reader.dictionary import Dictionary
from reader.cleaner import Cleaner
from tokenizing import Tokenizer


class FileReader:
    def __init__(self, path, matches_path):
        sheet = pd.read_excel(path)
        self.articles = []
        self.dict = Dictionary()
        self.tokenizer = Tokenizer(matches_path)
        self.cleaner = Cleaner()
        for article in sheet.itertuples(True, 'Article'):
            self.articles.append(article)
            text = self.cleaner.clean(str(article.title))
            text += self.cleaner.clean(str(article.summary))
            text += self.cleaner.clean(str(article.content))
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
        for token in query_tokens:
            if token[0] == '!' and len(token) > 1:
                token = token[1:]
                res_not.append(self.dict.get(token))
            else:
                res.append(self.dict.get(token))
        if len(res) == 0:
            return []
        final = set(res[0])
        for i in range(1, len(res)):
            final = final.intersection(set(res[i]))
        for n in res_not:
            final = final - set(n)
        return self.get(final), query_tokens


if __name__ == '__main__':
    file_reader = FileReader('../data/IR-F19-Project01-Input.xlsx', '../matches.json')
    docs = file_reader.search("تست برای")
    for doc in docs:
        print(doc)
