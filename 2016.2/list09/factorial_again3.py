#https://www.urionlinejudge.com.br/judge/pt/problems/view/1429

fact_values = [1, 1, 2, 6, 24, 120, 720, 5040]

num = raw_input()
size = len(num)
while (num != '0'):
    result = 0
    for i in xrange(size):
        result += int(num[i]) * fact_values[size - i]
    print result
    num = raw_input()
    size = len(num)
