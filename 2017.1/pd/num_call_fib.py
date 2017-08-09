#https://www.urionlinejudge.com.br/judge/pt/problems/view/1029

call = 40 * [0]
fib = 40 * [0]
fib[1] = 1
call[2] = 1

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
        return 1 
    elif(call[num] != 0):   
        return call[num]
    else:
        result = fib_call(num - 1) + fib_call(num - 2)+1
        call[num] += result
        return result

tests = int(raw_input())
for i in xrange(tests):
    num = int(raw_input())
    result = fib_value(num)
    calls = fib_call(num)
    print  result
    print calls
    print call
