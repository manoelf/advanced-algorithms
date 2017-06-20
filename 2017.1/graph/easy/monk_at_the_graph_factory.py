#https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-at-the-graph-factory/

vertices = int(raw_input())
degrees = map(int, raw_input().split())

edges = sum(degrees)/2.0

calc = vertices - 1
if (edges == calc):
    print "Yes"
else:
    print "No"
