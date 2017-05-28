#https://www.hackerrank.com/contests/basico-2017-1-lista-2/challenges/reduced-string

string = raw_input()

def verify(string):
    for i in xrange(len(string) - 1):
        if (string[i] == string[i + 1]):
            return False
    return True

def reduces(string):
    new = ''
    size = len(string)
    i = 0
    shift = 0
    while (i < size - 1):
        if (string[i] == string[i+1]):
            i += 2
        else:
            new += string[i]
            i += 1
    if (i == size - 1):
        new += string[-1]

    return new

word = reduces(string)

while (not(verify(word))):
    word = reduces(word)

if (word == ''):
    print 'Empty String'
else:
    print word
        
    

