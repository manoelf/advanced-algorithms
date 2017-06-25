#https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-learning-graph-3/

tests = int(raw_input())

for i  in xrange(tests):
    graph = {}
    vertice, edge = raw_input().split()
    depd = map(int, raw_input().split())
    print edge
