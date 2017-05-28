#http://codeforces.com/problemset/problem/570/B

# 1.. n : range
# m : misha choose
# a : andrew choose
# c : random choose

# |c - a| < |c - m|

def calc(m, middle):
    if (m < middle):
        result = m + 1
    else: 
        result = m - 1
    return result


n, m = map(int, raw_input().split())
if (n == 1):
    a = 1
elif (n % 2 == 1):
    meio = n/2
    if (m == meio):
        a = meio + 1
    else:
        a = calc(m, meio)
else:
    meio = n/2 + 1
    if (m == meio):
        a = meio - 1
    else:
        a = calc(m, meio)


print a
