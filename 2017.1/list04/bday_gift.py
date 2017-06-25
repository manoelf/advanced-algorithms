#https://www.hackerrank.com/contests/basico-2017-1-lista-4/challenges/bday-gift

n = int(raw_input())
some = 0

for i in xrange(n):
    some += int(raw_input())

print "%.1f" % (some/2.0)

