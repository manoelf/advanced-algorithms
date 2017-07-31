#http://practice.geeksforgeeks.org/problems/maximum-sub-array/0

import sys 

def max_sub(array, n):
    maxi = 0 
    max_here = maxi
    first = 0
    second = 0
    started = False
    for i in range(n):
        if (array[i] + max_here > 0):     
            max_here += array[i]
            if (not(started) and first == 0):
                first = i
                started = True
        else:
            max_here = 0
            started = False
        if (max_here > maxi):
            maxi = max_here
            last = i
    print maxi
    print first, second
    return first, second

def format(array):
    for i in array:
        print i,

t = int(raw_input())
for i in range(t):
    size = int(raw_input())   
    array = map(int, raw_input().split())
    x, y = max_sub(array, size)
    format(array[x:y+1])
    print "ended"
