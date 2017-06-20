#https://www.urionlinejudge.com.br/judge/pt/problems/view/1089
n = int(raw_input())
values = map(int, raw_input().split())

peaks = 1 
minor = True #values[1] < values[0]
major = True #values[1] > values[0]

for i in xrange(n):
    if (i > 0):
        if (values[i] > values[i - 1] and minor):
            minor = False
            major = True
            peaks += 1
        elif (values[i] < values[i -1] and major):
            major = False 
            minor = True
            peaks += 1




print peaks
