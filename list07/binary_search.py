#http://www.spoj.com/problems/BSEARCH1/


def binary_search(num, start, end):
    middle = (start + end) / 2
    if (start > end):
        return -1
    elif (array[middle] == num):
        return middle
    elif (array[middle] < num):
        return binary_search(num, middle + 1, end)
    elif (array[middle] > num):
        return binary_search(num, start, middle - 1)
    
    

n, q = map(int, raw_input().split())

array = map(int, raw_input().split())

for i in xrange(q):
    num = int(raw_input())
    print binary_search(num, 0, n-1)


