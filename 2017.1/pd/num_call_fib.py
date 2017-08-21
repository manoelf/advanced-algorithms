#https://www.urionlinejudge.com.br/judge/pt/problems/view/1029

call = 40 * [0]
fib = 40 * [0]
fib[1] = 1
call[2] = 2

def fib_value(num):
    if (num == 0):
        return 0
    elif (fib[num] != 0):
        return fib[num] 
    else:
        value = fib_value(num - 1) +  fib_value(num - 2) 
        fib[num] = value
        return value 

def fib_call(num):
    if (num <= 1):
        return  0
    elif(call[num] != 0):   
        return call[num] + 1
    else:
        call[num] = fib_call(num - 1) + fib_call(num - 2) + 1
        return call[num] 

tests = int(raw_input())
for i in xrange(tests):
    call = 40 * [0]
    call[2] = 2
    num = int(raw_input())
    result = fib_value(num)
    calls = fib_call(num)
    print "fib(%d) = %d calls = %d" % (num, calls, result) 
