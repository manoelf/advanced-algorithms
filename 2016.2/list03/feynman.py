#https://www.urionlinejudge.com.br/judge/pt/problems/view/1323

num = int(raw_input())


while (num != 0):
    result = 0
    for i in xrange(1, num + 1, 1):
        result += i*i
    print result
    num = int(raw_input())



