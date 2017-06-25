#https://www.hackerrank.com/contests/basico-2017-1-lista-3/challenges/closest-number

import math 

def find_closest(a, b, x):
    if (b < 0):
        return 0
    else:
        num = math.pow(a, b)
        if (num == 1):
            return 1
        i = num - 1
        while (i > 1 or i/x == 0):
            if (i % x == 0):
                return i
            i -= 1
    return 0
            

n = int(raw_input())
for i in xrange(n):
    a, b, x = map(int, raw_input().split())
    result = find_closest(a, b, x)
    print int(result)
