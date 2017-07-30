#https://www.urionlinejudge.com.br/judge/pt/problems/view/1151


mem = [0 for i in xrange(50)]
mem[1] = 1


def fib(num):
    if (mem[num] != 0):
        return mem[num]
    elif (num < 2):
        return mem[num]
    else:
        mem[num] = fib(num - 1) + fib(num - 2)
        return mem[num]


num = int(raw_input())

fib(num - 1)
for i in xrange(num):
    print mem[i],
