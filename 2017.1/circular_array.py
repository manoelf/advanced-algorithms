
def get_value(array, n, k, m):
    mod =  k % n
    return array[-mod + m] 


n, k, q = map(int, raw_input().split())
array = map(int, raw_input().split())

for i in xrange(q):
    m = int(raw_input())
    print get_value(array, n, k, m)



