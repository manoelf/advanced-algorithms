#https://www.urionlinejudge.com.br/judge/en/problems/view/2178


values = raw_input().split(" ")

birds = int(values[0])
places = int(values[1])


laps = 0
for i in range(birds):
    positions = raw_input().split(" ")
    n = int(positions[0])
    total = 0
    for i in range(1, n):
        if (n > 1 && i < total - 1):
            if (positions[i]  < positions[i-1]):
                total += (n - positions[i - 1]) + positions[i]
            else:
                total += positons[i]
        else:
            total += positions[i]
    

print laps









