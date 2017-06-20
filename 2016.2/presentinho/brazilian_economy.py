#https://www.urionlinejudge.com.br/judge/en/problems/view/1796

q = int(raw_input())

values = raw_input().split(" ")
count = 0
ok = False
for i in range(q):

    if (values[i] == '0'):
        count = count + 1
    if (count > (q/2)): 
        ok = True
        break

if (ok):
    print "Y"
else:
    print "N"
