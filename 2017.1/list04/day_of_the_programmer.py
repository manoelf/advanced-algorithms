#https://www.hackerrank.com/contests/basico-2017-1-lista-4/challenges/day-of-the-programmer

year = int(raw_input())
is_leap = False

if (year == 1918):
    print "26.09.%s" % year
elif ((year < 1917 and year % 4== 0) or (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):   
    print "12.09.%s" % year
else:
    print "13.09.%s" % year
