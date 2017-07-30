#http://practice.geeksforgeeks.org/problems/x-total-shapes/0
from collections import defaultdict

def dfs(u, start, visited):
    components = 0
    for v in u:
        if (not(visited[v])):
            visited[v] = True
            dfs(v, visited)
    for node in u:
        if (not(visited[node])):
            components += 1
            visited[node] = True
            dfs(node, visited)
    return components


def isX(matrix, i, j):
    return matrix[i][j] == x

def build(matrix, line, col, visited):
    graph = defaultdict(set)
    for i in range(line):
        for j in range(col):
            if (isX(matrix, i, j):
                graph[(i, j)] = set()
                if (i > 0):
                    if (isX(matrix, i - 1, j)
                        graph[(i, j)].add(i - 1, j)
                if (i + 1 < line):
                    if (isX(matrix, i + 1, j)):
                        graph[(i, j)].add(i + 1, j)
                if (j > 0):
                    if (isX(matrix, i, j - 1)):
                        graph[(i, j)].add(i, j - 1)

                if (j + 1 < col):
                    if (isX(matrix, i, j + 1)):
                        graph[(i, j)].add(i, j + 1)
                visited[(i, j)] = False

    return graph


                    
tests = int(input())

for i in range(tests):
    lin, col = input().split()
    value = input().split()
    graph[(0,0)] = set()
    visited = defaultdict
    graph = build(value, int(lin), int(col), visited)
    print(dfs(graph), (0,0), visited)
