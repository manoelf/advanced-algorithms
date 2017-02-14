#http://codeforces.com/problemset/problem/732/A


price, coin = map(int, raw_input().split())

cont = 0 
value = price
module = True


while (module):
    module = value%10 != 0 and  value%10 != coin
    cont += 1
    value += price

print cont
