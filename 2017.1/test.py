#coding: utf-8
import sys,os
n = int(raw_input())

maxValue = sys.maxint * -1
result = ['','']
while(n > 0):
    array = raw_input().split(',')
    notas_array = map(int,array[2: len(array)])
    value = sum(notas_array) / 3.0
    if(notas_array > maxValue):
        result[0] = array[0]
        result[1] = array[1]
    n -= 1

print result

