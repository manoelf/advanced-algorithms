#http://br.spoj.com/problems/OLIMPJ09/


pais, mod = map(int, raw_input().split())


clas = {}

for i in xrange(pais):
    clas[i] = 0
    


for i in xrange(mod):
    o, p , b = map(int, raw_input().split())
    clas[o-1] += 1
    clas[p-1] += 1
    clas[b-1] += 1

print clas
