#https://www.hackerrank.com/contests/basico-2017-1-lista-3/challenges/leonardo-and-prime
def is_prime(n):
    if (n == 2 or n == 3):
        return True
    if (n <= 1 or n%2 == 0):
        return False
    i = 3
    while (i*i <= n):
        if (n % i == 0):
            return False
        i += 2
    return True



def next_prime(num):
    new_num = num + 1
    while (not(is_prime(new_num))):
        new_num += 1
    return new_num

def find_divisors(value):
    primes = set()
    num = next_prime(1)
    total = 1 
    cont = 0
    while (total <= value):
        total *= num
        num = next_prime(num)
        cont += 1
    return cont








n = int(raw_input())
for i in xrange(n):
    value = int(raw_input())
    print find_divisors(value) - 1

    
    


