#http://codeforces.com/problemset/problem/659/A?csrf_token=c63d435484e15ca945a699243d442c7b

value = raw_input().split(" ")


a = int(value[0])
b = int(value[1])
c = int(value[2])

result =  (b + c) % a

if (result == 0):
    result = a 
print result
