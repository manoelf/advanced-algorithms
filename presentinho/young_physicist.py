#http://codeforces.com/problemset/problem/69/A

n = int(raw_input())

xi = 0
yi = 0
zi = 0

for i in range(n):
    values = raw_input().split(" ")
    xi += int(values[0])
    yi += int(values[1])
    zi += int(values[2])


if (xi == 0 and yi == 0 and zi == 0):
    print "YES"
else: 
    print "NO"




