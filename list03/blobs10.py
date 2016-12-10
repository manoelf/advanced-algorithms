#https://www.urionlinejudge.com.br/judge/pt/problems/view/1170

def calculate_days(food):
    count = 0
    while(food > 1.0):
        food -= food/2.0
        count += 1
    return count

n = int(raw_input())

for i in xrange(n):
    food = float(raw_input())
    print "%d dias" % calculate_days(food)




