#https://www.hackerrank.com/contests/basico-2017-1-lista-3/challenges/leonardo-and-prime
def is_prime(i):
    if (i == 1 or i == 3 or
         i == 5 or i == 7):
        return True
    #multiples of 2
    elif (i % 2 == 0):
        return False
    #divisible by 3
    elif (i % 3 == 0):
        return False
    #divisible by 5
    elif (i != 5 and i % 5 == 0):
        return False
    #divisible by 7
    elif (i != 7 and i % 7 == 0):
        return False
    else:
        return True
 
def print_primes(end):
    cont = 0
    for i in xrange(0, end + 1):
        if (is_prime(i)):
            cont += 1
            print i
    

n = int(raw_input())
for i in xrange(n):
    value = int(raw_input())
    print_primes(value)
    
    


