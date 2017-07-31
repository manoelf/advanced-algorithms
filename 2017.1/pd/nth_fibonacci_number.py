#http://practice.geeksforgeeks.org/problems/nth-fibonacci-number/0

n_fib = 10010 * [0]
n_fib[1] = 1
n_fib[2] = 1

def fib(n):
    if (n_fib[n] != 0):
        return n_fib[n]
    elif (n <= 1):
        return 1
    else:
        value = fib(n-1) + fib(n-2)
        n_fib[n] = value
        return value
t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    fib(n)
    print n_fib[n] % 1000000007

