#https://www.urionlinejudge.com.br/judge/pt/problems/view/2064

letters = {'a': 'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j','k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'x':'x', 'y':'y', 'z':'z', 'w':'w'}

frequence = {'a': 0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0,'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v': 0, 'x':0, 'y':0, 'z':0, 'w':0}


fav_size, name_size, swaps = map(int, raw_input().split())

fav = raw_input()
name = raw_input()

for i in name:
    frequence[i] += 1


def is_fav(letter):
    return letter in fav

def cont_fav(fav, frequence):
    total = 0
    for i in fav:
        total += frequence[i]
    return total

def existe(letter):
    if (frequence[letter] != 0):
        return True
    else:
        return False

best_name = letters.copy() 
max_fav = cont_fav(fav, frequence)


def swap(old, new, letters):
    for k in letters:
        if (letters[k] == old):
            letters[k] = new

def doble_swap(old, new, letters):
    for k in letters:
        if (letters[k] == old):
            letters[k] = new
        elif (letters[k] == new):
            letters[k] = old

total = 0
for i in xrange(swaps):
    first, second = raw_input().split()

    if (existe(first) and existe(second)):
        doble_swap(first, second, letters)
        frequence[first], frequence[second] = frequence[second], frequence[first]
    elif (not(existe(first)) and existe(second)):
        swap(second, first, letters)
        frequence[first] = frequence[second]
        frequence[second] = 0
    elif (existe(first) and not(existe(second))):
        swap(first, second, letters)
        frequence[second] = frequence[first]
        frequence[first] = 0
    
    total = cont_fav(fav, frequence)
    if (total > max_fav):
        max_fav = total
        best_name = letters.copy()
    

new_name = ""
for i in name:
    new_name += best_name[i]

print max_fav
print new_name
