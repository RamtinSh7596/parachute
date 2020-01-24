from math import log10, sqrt
from result.result import Result


def cosine_similarity(a, b):
    length = len(a)
    if len(b) != length:
        raise Exception('vectors length must be equal')
    similarity = 0
    for i in range(length):
        similarity += a[i] * b[i]
    a_size = sqrt(sum([i * i for i in a]))
    b_size = sqrt(sum([i * i for i in b]))
    similarity = similarity / (a_size * b_size)
    return similarity


def tf_idf(dictionary, size, tokens=None, document=None):
    for token in dictionary.tokens:
        if tokens is not None:
            term_frequency = tokens.count(token)
        elif document is not None:
            try:
                term_frequency = len(dictionary.get(token)[document])
            except KeyError:
                term_frequency = 0
        else:
            yield 0
            continue
        document_frequency = len(dictionary.get(token))
        if term_frequency == 0 or document_frequency == 0:
            yield 0
            continue
        tf = 1 + log10(term_frequency)
        idf = log10(size / document_frequency)
        yield tf * idf


if __name__ == '__main__':
    s = cosine_similarity(
        [3, 4],
        [4, 3],
    )
    print(s)
