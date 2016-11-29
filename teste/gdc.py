a = int(raw_input())
b = int(raw_input())


i = min(a,b)


while (i >= 1):
    if (a%i == 0 and b%i == 0):
        print i
        break
    i -= 1


def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

print gcd(a,b)

