V, E = map(int, raw_input().split())
V += 1

Q = set() # all vertices
S = [] #auxiliary to put teh vertices removes from Q
adj = {} # adjacence list for each vertices

prev = V * [None]
dist = V * [float("+infinity")]
w = {} #Graph maping vertice: weight
def populate_w(v1, v2, weight):
    edge =  (v1, v2)
    w[edge] = weight

def populate_adj(v1, v2):
    if (v1 in adj):
        adj[v1].add(v2)
    else:
        adj[v1] = set()
        adj[v1].add(v2)   
    if (v2 in adj):
        adj[v2].add(v1)
    else:
        adj[v2] = set()
        adj[v2].add(v1)
 

for i in xrange(E):
    v1, v2, weight = map(int, raw_input().split())
    populate_w(v1, v2, weight)
    populate_adj(v1, v2)
    Q.add(v1)
    Q.add(v2)


def extract_min(Q):
    mini = None
    vertice = None
    for v in Q:
        if (mini == None): 
            mini = dist[v]
            vertice = v
        elif (dist[v] < mini):
            mini = dist[v]
            vertice = v
    Q.remove(vertice)
    return vertice

dist[1] = 0
while (len(Q) > 0):
    print "Distances", dist
    print "Previous", prev
    print "Q", Q
    print "S", S

    u = extract_min(Q)
    S.append(u)
    print "u", u
    if (u == V): break
    
    for v in adj[u]:
        print (u, v) in w
        if ((u, v) in w and dist[v] > dist[u] + w[(u, v)]):
            dist[v] = dist[u] + w[(u, v)]
            prev[v] = u
print "Distances", dist
print "Previous", prev
print "Q", Q
print "S", S
print "Adjacences", adj
print "Graph w", w
