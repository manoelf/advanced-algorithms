#http://codeforces.com/problemset/problem/507/B

import math

radio, q1, q2, p1, p2 = map(int, raw_input().split())

def cal_dist(q1, q2, p1, p2):
    result = ((q1-p1)**2 + (q2-p2)**2)**(0.5)
    return result
if (q1 == p1 and q2 == p2):
    print 0    
else:
    result = math.ceil(cal_dist(q1, q2, p1, p2)/(2*radio))
    print int(result)
