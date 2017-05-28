#http://codeforces.com/problemset/problem/260/A

a, b, n = map(int, raw_input().split())

def make_divisible(num):
    i = 0 
    new_num = num + str(i)
    while (i <= 9 and int(new_num) % b != 0):
        i += 1
        new_num = num + str(i)

    if (int(new_num) % b == 0):
        return new_num
    else:
        return num

result = str(a) 
i = 0
while (i < n and result == str(a)):
    result = make_divisible(result)
    i += 1

if (int(result) % b == 0):
    print result + ((n - i) * '0')
else:
    print -1
