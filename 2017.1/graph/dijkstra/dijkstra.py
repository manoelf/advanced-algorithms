#http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/

from collections import defaultdict

def mont_graph(matrix):
    graph = defaultdict(list)
    weight = 0
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            weight = matrix[i][j]
            if (weight):
                graph[i].append([j, weight])
                if (i != j):
                    graph[j].append(([i, weight]))
    return graph

matrix  = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ];

print mont_graph(matrix)
