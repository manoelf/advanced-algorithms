#http://codeforces.com/problemset/problem/831/B

first = raw_input()
second = raw_input()
word = raw_input()

alph = {}

for i in xrange(26):
    alph[first[i]] = i

result = ''
for i in word:
    if (i.lower() not in alph):
        result += i
    elif (i == i.upper()):
        result += second[alph[i.lower()]].upper()
    else:
        result += second[alph[i.lower()]]

print result
