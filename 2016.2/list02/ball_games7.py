#http://codeforces.com/problemset/problem/430/B


n, k, x = map(int, raw_input().split())
balls = map(int, raw_input().split())


def distroy_balls(array):
    go = True
    i = 0
    cont = 0
    while (go):
        size = len(array)
        if (i + 2 < size):
            temp = array[i]
            if (array[i] == array[i + 1] == array[i + 2]):
                while (i < size and array[i] == temp):
                    cont += 1
                    array.pop(i)
                    size -= 1
                i = 0
            else:
                i += 1
        else:
            go = False
    return cont

maxi = 0

for i in xrange(n - 1):
    if (balls[i] == balls[i + 1] == x):
        copy = balls[:]
        copy.insert(i, x)
        temp = distroy_balls(copy)
        if (temp > maxi):
            maxi = temp

if (maxi > 0):
    print (maxi - 1)
else:
    print 0
    



