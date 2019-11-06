import re
import pandas as pd
from file_reader.dictionary import Dictionary
from tokenizer import tokenizer


def clean_html(html):
    pattern = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    clean = re.sub(pattern, '', html)
    return clean


class FileReader:
    def __init__(self, path):
        sheet = pd.read_excel(path)
        self.articles = []
        self.dict = Dictionary()
        for article in sheet.itertuples(True, 'Article'):
            self.articles.append(article)
            text = clean_html(article.content)
            tokens = tokenizer.tokenize(text)
            pos = 0
            for token in tokens:
                self.dict.add(token, article.Index, pos)
                pos += 1

    def get(self, keys):
        for key in keys:
            yield self.articles[key]

    def search(self, query):
        query_tokens = list(tokenizer.tokenize(query))
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
    file_reader = FileReader('./data/IR-F19-Project01-Input.xlsx')
    file_reader.search("تست !برای")
