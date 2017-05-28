#https://www.hackerrank.com/contests/basico-2017-1-lista-2/challenges/big-sorting

import math

n = int(raw_input())
matriz = []

for i in xrange(n):
    num = int(raw_input())
    matriz.append([math.log(num), num])

new_matriz = sorted(matriz)

for i in xrange(n):
    print new_matriz[i][1]
        
