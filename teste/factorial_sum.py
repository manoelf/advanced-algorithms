#https://www.urionlinejudge.com.br/judge/pt/problems/view/1161
def factorial(a):
    if (a == 0):
        return 1
    return a * factorial(a - 1)

while (True):
    try:
        values = map(int, raw_input().split())
        print factorial(values[0]) + factorial(values[1])
    except: 
        break




