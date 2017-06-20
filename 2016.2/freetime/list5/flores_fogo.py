#https://www.urionlinejudge.com.br/judge/pt/problems/view/1039


def calc_distance(x1, y1, x2, y2):
    result = ((x1 - x2)**2 + (y1 -y2)**2)**(1.0/2.0)
    return result

while (True):
    try:
        r1, x1, y1, r2, x2, y2 = map(int, raw_input().split())

        if (calc_distance(x1, y1, x2, y2) + r2 > r1):
            print "MORTO"
        else:
            print "RICO"

    except:
        break



