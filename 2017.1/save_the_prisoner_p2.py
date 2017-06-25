#!/bin/python
#https://www.hackerrank.com/contests/basico-20171-lista-1/challenges/save-the-prisoner


t = int(raw_input())
for i in xrange(t):
    prisoners, sweets, pos = map(int, raw_input().split())
    module = sweets % prisoners
    if (module + pos > prisoners):
        result =  (module + pos) % prisoner
    else:
        result = module + pos
    
    result -= 1
    if (result == 0):
        print prisoners
    else:
        print result


