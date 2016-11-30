#http://codeforces.com/problemset/problem/660/A

def gcd(a, b):
    if (b == 0): return a;
    return gcd(b, a%b)

def find_num(a, b):
    num = 2
    while(gcd(a, num) != 1 and gcd(b, num) != 1):
        num += 1
    return num

n = int(raw_input())

array =  map(int, raw_input().split())

new_array = str(array[0])

cont = 1


for i in xrange(n - 1):
    new_array += " " + str(array[i])
    if (gcd(array[i], array[i + 1]) != 1):
        new_array += " " + str(find_num(array[i], array[i + 1]))
        cont += 1

new_array += " " + str(array[n-1])
print cont
print new_array

    
 
 
    


