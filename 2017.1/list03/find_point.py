#https://www.hackerrank.com/contests/basico-2017-1-lista-3/challenges/find-point

def find_reflection(a, b):
    result = (2*b[0] - a[0], 2*b[1] - a[1])
    return result


n = int(raw_input())
for i in xrange(n):
    points = map(int, raw_input().split())
    answer = find_reflection(points[0:2], points[2:4])
    print answer[0], answer[1]
