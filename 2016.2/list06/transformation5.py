#http://codeforces.com/problemset/problem/727/A

a, b = map(int, raw_input().split())

def found_num(a, b):
    sequence = []
    founded = False
    size = 0
    while (b >= a):
        sequence.append(int(b))
        size += 1
        if (b == a):
            founded = True
            break
        if (b % 2 == 0):
            b = b/2.0
        else:
            b = (b - 1)/10.0
    return founded, size, sequence
        
def print_result(result, size):
    sequence = str(result[size - 1])
    for i in xrange(size - 2, -1, -1):
        sequence += " " + str(result[i])
    return sequence


result = found_num(a, b)
founded = result[0]
size = result[1]
result_formated = print_result(result[2], size)

if (founded):
    print "YES"
    print size 
    print result_formated
else:
    print "NO"



    
