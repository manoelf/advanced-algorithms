#http://br.spoj.com/problems/SALDO13/

values = raw_input().split(" ")

days = int(values[0])
balance = int(values[1])
new_value = 0
min = balance

for i in range(days):
    new_value = int(raw_input())
    balance = balance + new_value

    if (balance < min):
        min = balance

print min
