n = int(raw_input())

array = map(int, raw_input().split())

found =  False
start = 0
end = 0

def reverse(start, end):
    index = start
    chang = (end - start) / 2
    while(start < end - chang):
        array[index],array[end] = array[end],array[index]
        end -= 1
        index += 1



for i in xrange(n - 1):
    if (array[i] > array[i+1] and not(found)):   
        start = i
        found = True
    if (found and array[i] < array[i + 1]):
        end = i
var = found 
reverse(start, end)
if (found):
    i = start
    while ( i < n -1):
        if (array[i] > array[i + 1]):
            found = False
            break
        i += 1
if (found or not(var)):
    print "yes"
    print "%d %d" % (start + 1, end + 1)
else:
    print "no"

