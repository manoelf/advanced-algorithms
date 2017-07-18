#https://www.urionlinejudge.com.br/judge/pt/problems/view/1029


mem = [0 for i in xrange(40)]
mem[1] = 1
total_call = [0 for i in xrange(40)]
total_call[1] = 1
total_call[2] = 2

def fib(num):
    if (mem[num] != 0):
        return mem[num]
    elif (num < 2):
        return mem[num]
    else:
        mem[num] = fib(num - 1) + fib(num - 2)
        if (num > 2):
            total_call[num] = total_call[num - 1] + total_call[num - 2]
        return mem[num]








tests = int(raw_input())
for i in xrange(tests):
    num = int(raw_input())
    result = fib(num)
 
    print "fib(%s) = %s calls = %s" % (num, total_call[num], result)
    print mem
    print total_call
