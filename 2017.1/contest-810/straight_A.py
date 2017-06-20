#http://codeforces.com/contest/810/problem/0

def calculate(n, k, array):
    cont = n 
    sume = 0
    for i in xrange(n):
        sume += array[i]
    
    while(sume/float(cont) < (k - 0.5)):
        sume += k
        cont += 1
    return cont


n, k = map(int, raw_input().split())
array = map(int, raw_input().split())

print calculate(n, k, array) - n

