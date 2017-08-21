#http://practice.geeksforgeeks.org/problems/shortest-path-from-1-to-n/0

def generate_graph(num):
    graph = {}
    for i in xrange(1, num + 1):
        if (i not in graph):
            graph[i] = set()
        if (i + 1 <= num): 
            graph[i].add(i + 1)
        if (3*i <= num):
            graph[i].add(3*i)
    return graph

def bsf(graph, visited, element):
    queue = [1]
    visited[1] = True
    cont = 0
    while (queue):
        
        print "queue", queue
        node = queue.pop(0)
        if (node == element):
            return cont
        cont += 1 
        visited[node] = True
        for i in graph[node]:
            if (i == element): return cont
            if (visited[i] == False):
                queue.append(i)
                visited[i] = True
    return cont

tests = int(raw_input())




for i in xrange(tests):
    num = int(raw_input())
    visited = (num + 1) *[False]
    graph = generate_graph(num)
    result = bsf(graph, visited, num)
    print result
    print visited 
    print graph
