#http://codeforces.com/problemset/problem/146/A
def sume(array):
    result = 0
    for i in array:
        result += int(i)
    return result


def get_real_num(n, num):
    for i in xrange(n):
        if (num[i] != '0'):
            return num[i:], n - i
    return [], 0

def equals_half(n, num):
    middle = n/2
    if (n == 0):
        return False
    return sume(num[:middle]) == sume(num[middle:])

def is_magic(n, num):
    for i in num:
        if (i != '7' or i != '4'):
            return False
    return True
n = int(raw_input())
numero = raw_input()
num = [] 
for i in numero:
    num.append(i)

real_num, n = get_real_num(n, num)


if (is_magic(n,real_num) and equals_half(n, num)):
    print 'YES'
else:
    print 'NO' 

