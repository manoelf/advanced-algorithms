# implementing the DFS algorithm using a adjacense matrix
# we have problems with a non conected graph, not all vertex will
# be visited

matrix = {1:[2, 4], 2:[1, 3, 6], 3:[2, 4, 6], 4:[1, 3], 5:[6], 6:[2, 3, 5], 9:[], 8:[7], 7:[8]}



visited = []

def DFS(vertex):
    for i in xrange(len(matrix[vertex])):
        item = matrix[vertex][i]
        if (item not in visited):
            visited.append(item)
            DFS(item)
    return visited

print DFS()

