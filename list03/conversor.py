a = raw_input()


result = 0
for i in xrange(len(a)):
    if (a[len(a) - 1 -i] == '1'):
        result += 2**i
print result
