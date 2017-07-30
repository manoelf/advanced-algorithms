

def bsf_connected(graph, start):
    visited = set()
    queue = [start]
    
    while queue:
        vertex = stack.pop(0)
        if (vertex not in visited):
            visited.add(vertex)
            visited.extend(graph[vertex] - visited)
    return visited
