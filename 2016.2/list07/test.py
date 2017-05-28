

adj = {}
def populate(edges):
    if (edges[0] in adj):
        adj[edges[0]].add(edges[1])
    else:
        adj[edges[0]] = set()

    if (edges[1] in adj):
        adj[edges[1]].add(edges[0])
    else:
        adj[edges[1]] = set() 

for i in xrange(10):
    e1, e2 = map(int, raw_input().split())
    populate((e1, e2))

print adj
