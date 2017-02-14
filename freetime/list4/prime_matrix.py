#http://codeforces.com/problemset/problem/271/B

#---- Crivo -----
size = 100010
primes  = size * [True]

primes[0] = False
primes[1] = False

for i in xrange(2, size, 1):
    if (primes[i]):
        for j in xrange(i*2, size, i):
            primes[j] = False

#------------------        

#--- Pass to make a prime matrix ---

lin, col = map(int, raw_input().split())

matriz = []

for i in xrange(lin):
    linha = map(int, raw_input().split())
    matriz.append(linha)


incrementos = {}

min_passos = float("Inf")

for i in xrange(lin):
    passos = 0
    for j in xrange(col):
        valor = matriz[i][j]
        if (primes[valor]):
            incrementos[valor] = 0
        elif (valor in incrementos):
            passos += incrementos[valor]
        else:
            cont = 0
            copia = matriz[i][j]
            while (not(primes[copia])):
                copia += 1
                cont += 1 
            passos += cont
            incrementos[valor] = cont
    if (passos < min_passos):
        min_passos = passos


for i in xrange(col):
    passos = 0
    for j in xrange(lin):
        passos += incrementos[matriz[j][i]]
    if (passos < min_passos):
        min_passos = passos
        
print min_passos




