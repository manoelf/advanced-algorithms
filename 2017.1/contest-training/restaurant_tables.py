#http://codeforces.com/problemset/problem/828/A

n, a, b = map(int, raw_input().split())
people = map(int, raw_input().split())

rejected = 0
missing = 0
for i in people:
    if (i == 1):
        if (a > 0):
            a -= 1
        else:
            if (b > 0):
                if (missing == 1):
                    missing -= 1
                    b -= 1
                else:
                    missing = 1

            else:
                rejected += 1
    else:
        if (b > 0):
            if (b == 1 and missing == 1):
                rejected += i
            else:
                b -= 1
        else:
            rejected += i
print rejected
