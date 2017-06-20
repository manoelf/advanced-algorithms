#https://www.urionlinejudge.com.br/judge/en/problems/view/1044

values = raw_input().split(" ")

max = 0
min = 0
a = int(values[0])
b = int(values[1])

if (a > b):
    max = a
    min = b
else:
    max = b
    min = a


if ((max%min) == 0):
    print "Sao Multiplos"
else:
    print "Nao sao Multiplos"

