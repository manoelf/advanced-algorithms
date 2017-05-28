pares = {}
def restart():
    for i in xrange(30, 61, 1):
        pares[i] = [0, 0]

try:
    while(True):
        restart()
        n = int(raw_input())
        for i in xrange(n):
            valor = raw_input().split()
            if (value[1] == "D"):
                pares[valor[0]][0] += 1
            else:
                pares[valor[1]][1] += 1
        print pares

except: 
    print "nada"    
    

