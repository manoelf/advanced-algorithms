#https://www.urionlinejudge.com.br/judge/pt/problems/view/1926

size = 10**6 + 10

primes = (1000010) * [True] 

primes[0] = False
primes[1] = False

for i in xrange(2, size,1):
    if (primes[i]):
        for j in xrange(i*2, size, i):
            primes[j] = False

twin_primes = (size) * [0]

for i in xrange(3, size - 2, 1):
    if (primes[i]  and (primes[i - 2] or primes[i + 2])):
        twin_primes[i] = 1
    twin_primes[i] += twin_primes[i - 1]


size = int(raw_input())

for i in xrange(size):
    init, end = map(int, raw_input().split())
    if (init > end):
        init, end = end, init
    print twin_primes[end] - twin_primes[init - 1]

