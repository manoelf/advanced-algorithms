#https://www.urionlinejudge.com.br/judge/pt/problems/view/1028

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

n = int(raw_input())

for i in range(n):
    values = map(int, raw_input().split())
    print gcd(values[0], values[1])


