a = map(int, raw_input().split())
a.sort()

area = 0
totalArea = 600 * 100

if (a[1] < a[0] + 200):
    if(a[2] < a[1] + 200):
        area = abs(a[0] - (a[2] + 200))
    else:
        area = abs(a[0] - (a[1] + 200)) + 200
else:
    if(a[2] < a[1] + 200):
        area = abs(a[1] - (a[2] + 200)) + 200
    else:
        area = 600
        
area = area * 100

print totalArea - area
