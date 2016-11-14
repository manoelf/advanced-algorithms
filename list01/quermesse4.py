#http://br.spoj.com/problems/QUERM/



cont = 0 
result = 0
while(raw_input() != "0"):
    values = raw_input().split(" ")
    
    for i in xrange(len(values)):   
        if (str(i + 1) == values[i]):
            result =  values[i]
            break
    cont += 1
    print "Teste %d" %cont
    print result
    print ""

 
