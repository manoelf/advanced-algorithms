#http://br.spoj.com/problems/COLISAO7/


sx0, sy0, sx1, sy1 = map(int, raw_input().split())

rx0, ry0, rx1, ry1 = map(int, raw_input().split())

if ((sx1 >= rx0 or sy1 >= ry0) and (sx0 <= rx1 and sy0 <= ry1)):
    print 1
else:
    print 0

