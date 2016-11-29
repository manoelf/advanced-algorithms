#http://codeforces.com/problemset/problem/260/A

a, b, n = map(int, raw_input().split())

def make_divisible(num):
    
    new_num = str(num) + '1'
    i = 2
    while (i <= 9 and int(new_num) % b != 0):
        new_num = num + str(i)
        i += 1
        
    if (int(new_num) % b == 0):
        return new_num
    else:
        return num

result = make_divisible(str(a))

for i in xrange(n - 1):
    result = make_divisible(result)


if (int(result) % 2 == 0):
    print result
else:
    print -1
