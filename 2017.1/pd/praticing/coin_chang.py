#https://www.youtube.com/watch?v=jaNZ83Q3QGc

coins = [1, 2, 5]

amount = 12

comb = (amount + 1) * [0]
comb[0] = 1

for c in coins:
    for amt in xrange(amount+1):    
        if (amt >= c):
            comb[amt] += comb[amt - c]

print comb[amount]
print comb
