#http://codeforces.com/problemset/problem/731/A



name = raw_input()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cont = 0
index = 0

for i in xrange(len(name)):
    local = letters.index(name[i])
    if (abs(local - index) >= 13):
        cont += len(letters) - abs(local - index)
    else:
        cont += abs(local - index)

    index = letters.index(name[i])

print cont

