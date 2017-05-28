#http://codeforces.com/problemset/problem/625/B

name = raw_input()
substring = raw_input()
size = len(substring)

cont = 0
i = 0

length = len(name)

while(i < length):
#    length = length + (size * cont)
    if (name[i: i + size] == substring):
        cont = cont + 1
        i = i + size
    else: 
        i = i + 1


print cont








