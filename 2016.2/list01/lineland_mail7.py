#http://codeforces.com/problemset/problem/567/A

n = int(raw_input())

cities = raw_input().split(" ")

cities = [int(num) for num in cities]



mini = abs(cities[1] - cities[0])

for i in range(n):
    if (i == 0):
        mini = abs(cities[1] - cities[0])
        maxi = abs(cities[n-1] - cities[0])

    if (abs(cities[n-1] -  cities[i]) > abs(cities[i] - cities[0])):
        maxi = abs(cities[n-1] -  cities[i])
    else:
        maxi = abs(cities[i] - cities[0])

    if (i <= n - 2):
        if (abs(cities[i + 1] -  cities[i]) < (abs(cities[i] - cities[i -1]))):
            mini = abs(cities[i + 1] -  cities[i])
        else:
            mini = (abs(cities[i] - cities[i -1]))
    else:
        mini = abs(cities[i] - cities[i-1])
    print "%d %d" % (mini,maxi)
