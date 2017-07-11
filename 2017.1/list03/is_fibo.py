def fibo(n):
    if (n == 0 or n == 1): return True
    a, b = 0, 1
    i = 0
    while (True):
        a, b = b, a + b
        print b
        if (b == n):
            return True
        elif (b > n):
            return False
    return False


t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    if (fibo(n)):
        print "IsFibo"
    else:
        print "IsNotFibo"
