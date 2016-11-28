#http://codeforces.com/problemset/problem/315/B

values = map(int, raw_input().split())

array = map(int, raw_input().split())

cont = 0

for i in range(values[1]):
    options = map(int, raw_input().split())
    if (options[0] == 1):
        array[options[1] - 1] = options[2] - cont
    elif (options[0] == 2):
        cont += options[1]
    elif (options[0] == 3):
        print array[options[1] - 1] + cont

