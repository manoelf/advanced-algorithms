#https://www.urionlinejudge.com.br/judge/pt/problems/view/2064
def cont_favorit(name, favorites):
    cont = 0
    for i in name:
        if i in favorites:
            cont += 1

    return cont

k, m, n = map(int, raw_input().split())
favorites = raw_input()
name = raw_input()
best_name = name
temp_name = name

for i in xrange(n):
    old, new = map(str, raw_input().split())
    if (old in favorites):
        old, new = new, old    
    temp_name = temp_name.replace(old, new)

    if (new in favorites):
        if (cont_favorit(temp_name, favorites) > cont_favorit(best_name, favorites)):
            best_name = temp_name


print cont_favorit(best_name, favorites)
print best_name



