def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num -2)


for x in range(10):

    print fib(int(raw_input())) 
