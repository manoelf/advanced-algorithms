#http://codeforces.com/problemset/problem/141/A
from collections import defaultdict

guest = raw_input()
residence = raw_input()
pile = raw_input()

names_dict = defaultdict()

for i in pile:
    if (i in names_dict):
        names_dict[i] += 1
    else:
        names_dict[i] = 1


def find(names_dict, pile):
    for i in (guest+residence):
        if (i in names_dict):
            if (names_dict[i] >= 1):
                names_dict[i] -= 1
            else:
                return 'NO'
        else:
            return 'NO'
    return 'YES'
if (len(guest+residence) != len(pile)):
    print 'NO'
else:
    print find(names_dict, pile)
