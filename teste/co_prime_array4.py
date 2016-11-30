#http://codeforces.com/problemset/problem/660/A

def gcd(a, b):
    if (b == 0): return a;
    return gcd(b, a%b)

n = int(raw_input())

array =  map(int, raw_input().split())

new_array = str(array[0])



for i in xrange(n - 1):
    new_array += " "
    if (gcd(array[i], array[i + 1]) != 1):
        
 
 
    


