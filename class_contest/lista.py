lista = []

n, k= map(int, raw_input().split())


for i in xrange(n):
    lista.append(raw_input())
lista.sort()

print lista[k -1]
