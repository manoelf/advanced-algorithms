#http://codeforces.com/contest/814/problem/0

n, k = map(int, raw_input().split())
origin_seq = map(int, raw_input().split())

poss_seq = map(int, raw_input().split())


poss_seq.sort()

j = k

for i in xrange(n):
    if (origin_seq[i] == 0):
        if (j - 1 >= 0):
            origin_seq[i] = poss_seq[j - 1]
            j -= 1
ok = False
for i in xrange(n - 1):
    if (origin_seq[i] > origin_seq[i + 1]):
        ok = True
        break

if (ok):
    print "Yes"
else:
    print "No"
