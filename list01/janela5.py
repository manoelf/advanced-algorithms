#http://br.spoj.com/problems/JANELA13/
values = [int(x) for x in raw_input().split(" ")]

values.sort()

f1 = values[0]
f2 = values[1]
f3 = values[2]

result = 0

if (f2 < (f1 + 200) ):
    result += (f1 + 200) - f2
if (f3 < (f2 + 200) ):
    result += (f2 + 200) - f3
if (f1 == f2 and f1 == f3):
    result = 400

print result * 100


