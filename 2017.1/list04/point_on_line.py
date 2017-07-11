#https://www.hackerrank.com/contests/basico-2017-1-lista-4/challenges/points-on-a-line

n = int(raw_input())

points = []

for i in xrange(n):
    x, y = map(int, raw_input().split())
    points.append((x, y))
x_verify = True
y_verify = True

for i in xrange(1, n):
    if (points[i - 1][0] != points[i][0]):
        x_verify = False
    if (points[i - 1][1] != points[i][1]):
        y_verify = False
    
if (x_verify or y_verify):
    print "YES"
else:
    print "NO" 
