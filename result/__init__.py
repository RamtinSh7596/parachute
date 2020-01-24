from math import log10, sqrt
from result.result import Result


def cosine_similarity(a, b):
    # length = len(a)
    # if len(b) != length:
    #     raise Exception('vectors length must be equal')
    # similarity = 0
    # for i in range(length):
    #     similarity += a[i] * b[i]
    # a_size = sqrt(sum([i * i for i in a]))
    # b_size = sqrt(sum([i * i for i in b]))
    # similarity = similarity / (a_size * b_size)
    # return similarity
    # return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(a))
    similarity = 0
    for t, s1 in a.items():
        try:
            s2 = b[t]
            similarity += s1 * s2
        except KeyError:
            pass
    a_norm = sqrt(sum([i * i for _, i in a.items()]))
    b_norm = sqrt(sum([i * i for _, i in b.items()]))
    return similarity / (a_norm * b_norm)


def tf_idf(dictionary, size, tokens=None, document=None):
    r = {}
    for index, token in enumerate(dictionary.tokens):
        if tokens is not None:
            term_frequency = tokens.count(token)
        elif document is not None:
            try:
                term_frequency = len(dictionary.get(token)[document])
            except KeyError:
                term_frequency = 0
        else:
            continue
        document_frequency = len(dictionary.get(token))
        if term_frequency == 0 or document_frequency == 0:
            continue
        tf = 1 + log10(term_frequency)
        idf = log10(size / document_frequency)
        r[index] = tf * idf
    return r


if __name__ == '__main__':
    x = {1: 4, 3: 2, 5: 3}
    y = {1: 3, 2: 1, 5: 4}
    s = cosine_similarity(x, y)
    print(s)
