#http://codeforces.com/problemset/problem/831/A

def is_unimodal(array, n):
    inc = False
    dec = False
    cost = False
    for i in xrange(n - 1):
        if (array[i] < array[i + 1] and dec == False and cost == False):
            inc  = True
        elif (array[i] == array[i + 1] and dec == False):
            cost = True
        elif (array[i] > array[i + 1]):
            dec = True
        elif (array[i] < array[i + 1] and cost == True):
            return False
        else:
            return False
    return True

n = int(raw_input())
array = map(int, raw_input().split())

if (is_unimodal(array, n)):
    print 'YES'
else:
    print 'NO'


