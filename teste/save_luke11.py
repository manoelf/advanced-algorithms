#http://codeforces.com/problemset/problem/624/A

d, l, v1, v2 = map(float, raw_input().split())

result = (l - d)/(v1 + v2)

print "%.20f" % result
