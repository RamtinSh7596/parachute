import re
import pandas as pd

sheet = pd.read_excel('./data/IR-F19-Project01-Input.xlsx')

regex = r'["!.،۰,:;&#<=>()+-/%_\n]|&nbsp;|\u200c|[a-zA-Z0-9۰-۹]'
tokens = {}
articles = []

for row in sheet.itertuples(True, 'Article'):
    articles.append(row)
    t = filter(lambda x: x != '', re.sub(regex, ' ', row.content).split(' '))
    for token in t:
        try:
            tokens[token].index(row.Index)
        except ValueError:
            tokens[token].append(row.Index)
        except KeyError:
            tokens[token] = [row.Index]

frequent_tokens = []

for token in tokens:
    f = len(tokens[token])
    if f / len(articles) > 0.8:
        frequent_tokens.append(token)
    tokens[token].sort()
    tokens[token] = {
        'f': f,
        'docs': tokens[token],
    }


def array_subscript(arrays):
    if len(arrays) == 0:
        return []
    if len(arrays) == 1:
        return arrays[0]
    x = arrays[0]
    y = array_subscript(arrays[1:])
    z = []
    x_ptr, y_ptr = 0, 0
    while x_ptr < len(x) and y_ptr < len(y):
        if x[x_ptr] == y[y_ptr]:
            z.append(x[x_ptr])
            x_ptr = x_ptr + 1
            y_ptr = y_ptr + 1
        elif x[x_ptr] > y[y_ptr]:
            y_ptr = y_ptr + 1
        else:
            x_ptr = x_ptr + 1
    return z


def search(query: str):
    query_tokens = filter(lambda x: x != '', re.sub(regex, ' ', query).split(' '))
    arrays = []
    for q_token in query_tokens:
        try:
            arrays.append(tokens[q_token]['docs'])
        except KeyError:
            return []
    return array_subscript(arrays)


def get_docs(indexes):
    for i in indexes:
        yield articles[i]