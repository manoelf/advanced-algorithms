#http://codeforces.com/problemset/problem/580/B


values = map(int, raw_input().split())

n = values[0]
friendship = 0
greater = 0
total_money = 0


for i in xrange(n):
    friend = map(int, raw_input().split())
    if (friend[1] > greater):
        greater = friend[1]
    friendship += friend[1]
    total_money += friend[0]

amount = values[1]

if (total_money/n >= amount):
    print greater
else:
    print friendship 



