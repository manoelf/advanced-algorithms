mem = 40 * [0]
mem[1] = 1
def fib(num):
    if (num == 0):
        return 0
    elif (mem[num] != 0):  
        return mem[num]
    else:
        mem[num] = fib(num - 1) + fib(num - 2)
        return mem[num]

print fib(int(raw_input()))
