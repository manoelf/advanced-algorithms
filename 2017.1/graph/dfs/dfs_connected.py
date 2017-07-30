#http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

def dfs_connected(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if (vertex not in visited):
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

graph = {1: set([2, 3]),
         2: set([1, 4, 5]),
         3: set([1, 6]),
         4: set([2]),
         5: set([2, 6]),
         6: set([3, 5])}

graph2 = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print dfs_connected(graph2, 'C') 
