#http://codeforces.com/problemset/problem/520/B

a, b = map(int, raw_input().split())

def find_num(a, b):
    result = 0
    if (a > b):
        result = a - b
    elif (b % 2 == 0):  
        while (a != b):
            if (a * 2 > b):
                result += 1
                a -= 1
            else:
                a = a*2
                result += 1
    else:
        while (a != b):
            if (a - 1 == b):
                result += 1
                break
            elif (a > b):
                result += a - b
                a = a - b
                break
            else:
                a = a * 2
                result += 1            
    return result

print find_num(a,b)


