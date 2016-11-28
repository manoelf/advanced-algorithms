#https://www.urionlinejudge.com.br/judge/en/problems/view/1091

n = int(raw_input())
while (n != 0 ):
    point = map(int, raw_input().split())

    for i in range(n):
        values = map(int, raw_input().split())
        x = values[0] - point[0]
        y = values[1] - point[1]
        if (x == 0 or y == 0):
            print "divisa"
        elif (x < 0 and y > 0):
            print "NO"
        elif (x > 0 and y > 0):
            print "NE"
        elif (x < 0 and y < 0):
            print "SO"
        elif (x > 0 and y < 0):
            print "SE"
    n = int(raw_input())








