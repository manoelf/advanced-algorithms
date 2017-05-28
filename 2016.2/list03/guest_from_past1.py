#http://codeforces.com/problemset/problem/625/A
#by Brito
money = int(raw_input())
plastic = int(raw_input())
glass = int(raw_input())
back = int(raw_input())

total_bottle = 0
real_price = glass - back

if (real_price< plastic):
    if (money >= glass):
        total_bottle = ((money - glass) / (glass - back)) + 1
        money -= total_bottle * real_price

total_bottle += money/plastic    
    

print total_bottle
            


