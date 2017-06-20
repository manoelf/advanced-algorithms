#https://www.urionlinejudge.com.br/judge/pt/problems/view/1018



n = int(raw_input())

print n

hundred = n / 100
remainder = (n % 100)
fifty = remainder / 50
remainder = remainder % 50
twenty = remainder / 20
remainder = remainder % 20
ten = remainder / 10
remainder = remainder % 10
five = remainder / 5
remainder = remainder % 5
two = remainder / 2
remainder = remainder % 2
one = remainder


print "%i nota(s) de R$ 100,00" %(hundred)
print "%i nota(s) de R$ 50,00" %(fifty)
print "%i nota(s) de R$ 20,00" %(twenty)
print "%i nota(s) de R$ 10,00" %(ten)
print "%i nota(s) de R$ 5,00" %(five)
print "%i nota(s) de R$ 2,00" %(two)
print "%i nota(s) de R$ 1,00" %(one)





