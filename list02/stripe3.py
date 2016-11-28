#http://codeforces.com/problemset/problem/18/C?locale=en

n = int(raw_input())
numbers = map(int, raw_input().split())

sume = 0

acomulated = []
for i in numbers:
    sume += i
    acomulated.append(sume)
total = acomulated[n-1]
result = 0
for i in xrange(n):
    sume = acomulated[i]
    if (i < (n - 1)):
        if ((total - sume) == sume):  
            result += 1

print result



