#http://www.spoj.com/problems/BSEARCH1/


def binary_search(init, end, num, result):
    mid = (init + end) / 2
    if (init > end):
        return -1
    elif (array[mid] == num):
        result = mid
    elif (array[mid] < num):
        return binary_search(mid + 1, end, num, result)
    elif (array[mid] > num):
        return binary_search(init, mid - 1, num, result)
    
size, ope = map(int, raw_input().split())
array = map(int, raw_input().split())

for i in xrange(ope):
    num = int(raw_input())
    print binary_search(0, size-1, num)

