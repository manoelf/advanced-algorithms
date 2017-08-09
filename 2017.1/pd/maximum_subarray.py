#http://practice.geeksforgeeks.org/problems/maximum-sub-array/0

import sys 

def max_sub(array, n):
    maxi = 0 
    max_here = maxi
    first = 0
    second = 0
    index = []
    for i in range(n):
        if (array[i] + max_here > 0):     
            max_here += array[i]
            if (len(index) == 0):
                index.append(i)
        else:
            max_here = 0
            index = []
        if (max_here > maxi):
            maxi = max_here
            index.append(i)
    return index

def format(array):
    for i in array:
        print i,

t = int(raw_input())
for i in range(t):
    size = int(raw_input())   
    array = map(int, raw_input().split())
    x, y = max_sub(array, size)
    format(array[x:y+1])
