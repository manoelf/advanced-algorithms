#https://www.urionlinejudge.com.br/judge/pt/problems/view/1307
def convensor(a):
    result = 0
    for i in xrange(len(a)):
        if (a[len(a) - 1 -i] == '1'):
            result += 2**i
    return result

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

n = int(raw_input())

for i in xrange(n):
    s1 = convensor(raw_input())
    s2 = convensor(raw_input())
    
    if (gcd(s1, s2) != 1):
        print "Pair #%d: All you need is love!" % (i + 1)    
    else:
        print "Pair #%d: Love is not all you need!" % (i + 1)


