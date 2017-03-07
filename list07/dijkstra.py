#http://codeforces.com/problemset/problem/20/C

vertices, edges = map(int, raw_input().split())
vertices  += 1

dad = vertices * [None]
distance = vertices * [float("+infinity")]
adj = {}

S = [] #definitive distance
Q = [] #vertices | provisore distances

w = {} 
V = set()

way = []

def populate(v1, v2):
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




for i in xrange(edges):
    v1, v2, weight = map(int, raw_input().split())
    populate(v1, v2)
    w[(v1, v2)] = weight
    V.add(v1)
    V.add(v2)
#w = {} will be the graph (1, 2): 9

for i in V:
    Q.append(i)

def extract_min(Q):
    mini = None
    for i in xrange(len(Q)):
        if (mini == None):
            mini = i
        elif (Q[i] < Q[mini]):
            mini = i
    return Q.pop(mini)

def dijkstra(V, start):
    distance[start] = 0
   # Q = V
    S = []

    while (len(Q) > 0):
        u = extract_min(Q)
        S.append(u)
        for v in adj[u]:
            print "dad:", dad
            print "distance:", distance
            print "Q:", Q
            print "S:", S
            print "u:", u
            print ""


            if ((u,v) in w and distance[v] > (distance[u] + w[(u,v)])):
                distance[v] = distance[u] + w[(u,v)]
                dad[v] = u
                way.append(v)
print dad
dijkstra(V, 1)
print "way:", way


