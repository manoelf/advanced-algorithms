#Implementing a DFS

# Dictionary will be used for the graph
from collections import defaultdict

class Graph:
    # Constructor    
    def __init__(self):
        self.graph = defaultdict(list) # Will storage the graph

    def addEdge(self, u, v): # method to add a edge to graph
        self.graph[u].append(v)

    def DFSUtil(self, v, visited): # Recution to reach all vertices .. from the adjacences 
        visited[v] = True
        print v # printing the current vertice
        
        for vertex in self.graph[v]: # walking for all adjacent vertex
            if (visited[vertex] == False):
                self.DFSUtil(vertex, visited)
    

    

    def DFS(self):
        V = len(self.graph)

        visited = [False] * V
            
        for i in xrange(V):
            if (not(visited[i])):
                self.DFSUtil(i, visited)


g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS()
