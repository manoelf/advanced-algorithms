#http://codeforces.com/contest/837/problem/0

def cont_vol_word(word):
    cont = 0
    for i in word:
        if (i == i.upper()):
            cont += 1
    return cont

def cont_vol_text(array):
    maxi = 0
    vol = 0
    for i in array:
        vol = cont_vol_word(i)
        if (vol > maxi):
            maxi = vol
    return maxi

n = int(raw_input())
text = raw_input().split()

print cont_vol_text(text)
