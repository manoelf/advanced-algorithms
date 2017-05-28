#http://codeforces.com/contest/810/problem/B

def calc(products, clients):
    products *= 2
    if (clients > products):
        return products
    else:
        return clients

n, days = map(int, raw_input().split())

day_options = []
length = 0

total = 0
for i in xrange(n):
    products, clients = map(int, raw_input().split())
    total += min(products, clients)
    result = calc(products, clients)

    if (result > 0):
        day_options.append((result, products, clients))
        length += 1
day_options.sort()

    
for i in xrange(length - 1, length - days - 1, -1):
    total -= min(day_options[i][1], day_options[i][2])
    total += day_options[i][0]

print total
