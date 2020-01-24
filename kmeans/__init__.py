import random
import sys
import numpy as np
# from reader import FileReader


def distance(x, y):
    return np.linalg.norm(np.array(x) - np.array(y))


def k_means(vectors, length, k, max_iter=None):
    centers = np.zeros(k, dtype=list)
    for i in range(k):
        r = random.randint(0, len(vectors) - 1)
        centers[i] = vectors[r]
    clusters, cluster_idx = None, None
    change = True
    if max_iter is None:
        max_iter = 20
    it = 0
    print('before while')
    while change and it < max_iter:
        print('iteration', it)
        change = False
        clusters = [[] for _ in range(k)]
        cluster_idx = [[] for _ in range(k)]
        # find cluster for each vector
        for i, vector in enumerate(vectors):
            dist, index = sys.maxsize, 0
            for j, center in enumerate(centers):
                d = distance(vector, center)
                if d < dist:
                    dist, index = d, j
            clusters[index].append(vector)
            cluster_idx[index].append(i)
        # find center of each cluster
        for i, cluster in enumerate(clusters):
            if len(cluster) == 0:
                centers[i] = 0
                continue
            centers[i] = np.average(cluster)
        it += 1
    return cluster_idx, centers


if __name__ == '__main__':
    # start_reading = time.time()
    # reader = FileReader('../data/IR-F19-Project01-Input.xlsx', True, '../matches.json', '../exceptions.txt')
    # end_reading = time.time()
    # print('Reading', end_reading - start_reading)
    # start_clustering = time.time()
    # k_means(reader.tf_idfs, len(reader.dict.tokens), 20)
    # end_clustering = time.time()
    # print('Clustering', end_clustering - start_clustering)
    a = np.array([
        [1, 2, 3],
        [1, 3, 1],
        [1, 2, 1],
        [10, 12, 3],
        [10, 11, 2],
    ])
    clusters, centers = k_means(a, 3, 2, 20)
    print(clusters)
    print(centers)
