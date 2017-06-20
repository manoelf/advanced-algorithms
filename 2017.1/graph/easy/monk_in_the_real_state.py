#https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-in-the-real-estate/

tests = int(raw_input())

for i in xrange(tests):
    edges = int(raw_input())
    cities = set()
   
    for i in xrange(edges):
        a, b = raw_input().split()
        cities.add(a)
        cities.add(b)
    print len(cities)
    
