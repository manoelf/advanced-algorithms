#http://codeforces.com/problemset/problem/520/B

a, b = map(int, raw_input().split())

def get_num(a, b):
    cont = 0

    while(a > 0):
        if (a == b):
            break
        elif (a < b):
    cont += 1
    return cont           

print get_num(a, b)
