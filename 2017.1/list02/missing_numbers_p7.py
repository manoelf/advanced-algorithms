#https://www.hackerrank.com/contests/basico-2017-1-lista-2/challenges/missing-numbers

n1 = int(raw_input())
array1 = map(int, raw_input().split())

n2 = int(raw_input())
array2 = map(int, raw_input().split())

freq1 = 1000020 * [0]
freq2 = 1000020 * [0]

result = []

for i in xrange(max(n1, n2)):
    if (i < n1):
        freq1[array1[i]] += 1
    if (i < n2):
        freq2[array2[i]] += 1	

for i in xrange(1000020):
    if (freq1[i] != freq2[i]):
        result.append(i)
result.sort()

out = ''
for i in result:
    out += str(i) + " "

print out[:-1:]

