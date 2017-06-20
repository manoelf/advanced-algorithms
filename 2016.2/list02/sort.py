#http://codeforces.com/contest/451/problem/B


n = int(raw_input())

array = map(int, raw_input().split())

init = -1
end = -1
increase = True

for i in xrange(n - 1):
    
    if (array[i] > array[i + 1] and init == -1):
        init = i
    elif (array[i] < array[i + 1] and init != -1 and end == -1):
        end = i
    elif (array[i] > array[i + 1] and init != -1 and end != -1):
        increase = False
    elif (array[i] < array[i + 1] and init != -1 and end != -1 and array[init] > array[i]):
        increase = False


if (init != -1 and end != -1 and array[n - 1] < array[init]):
    increase = False


if (init != -1 and end == -1):
    if (init - 1 >= 0 and array[init - 1] < array[n -1]):
        end = n - 1
    elif (init - 1 < 0):
        end = n - 1

for i in xrange(n - 1):
    if (i < init and array[i] > array[i + 1]):
        increase = False
    elif (i > end and array[i] > array[i + 1]):
        increase = False
    elif (i >= init and i < end and array[i] < array[i + 1]):
        increase =  False


if (init != -1 and end != -1 and increase):
    print "yes"
    print "%d %d" % (init + 1, end + 1)
elif (init == -1 and end == -1 and increase):
    print "yes" 
    print 1, 1
else:
    print "no"

