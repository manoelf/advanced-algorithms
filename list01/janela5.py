#http://br.spoj.com/problems/JANELA13/

sizes = raw_input().split(" ")
sizes = [int(num) for num in sizes]
sizes.sort()

f1 = sizes[0]
f2 = sizes[1]
f3 = sizes[2]

result = 0

if (f2 < (f1 + 200)):
    result = (f1 +200) - f2
if (f3 < (f2 + 200)):
    result += (f2 + 200) - f3

if (f1 == f2 or f1 == f3 or f2 == f3):
    result += 200

if (f1 == f2 and f1 == f3):
    result = 400
   
print result * 100

