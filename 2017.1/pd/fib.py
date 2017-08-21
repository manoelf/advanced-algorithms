calls = 40 * [0]
calls[2] = 2

def fib(num):
    if (num <= 1):
        return 0 
    elif (calls[num] != 0):
        return calls[num] + 1
    else:
        calls[num] = fib(num - 1) + fib(num - 2) + 1
        return calls[num]

num = int(raw_input())
fib(num)
print calls[num]
print calls 
