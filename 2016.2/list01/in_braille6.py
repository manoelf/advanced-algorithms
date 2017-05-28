#https://www.urionlinejudge.com.br/judge/en/problems/view/1357


letters1 = ['.*', '*.', '*.', '**', '**', '*.', '**', '**', '*.', '.*']
letters2 = ['**', '..', '*.', '..', '.*', '.*', '*.', '**', '**', '*.']


total = raw_input()
while (total != '0'):
    result = ""
    out1 = ""
    out2 = ""
    out3 = ""


    option = raw_input()

    if (option == 'S'):
        values = raw_input()
        for i in range(len(values)):
            out1 += letters1[int(values[i])] + " "
            out2 += letters2[int(values[i])] + " "
            out3 += '.. '


        print out1[:len(out1) - 1] 
        print out2[:len(out2) - 1] 
        print out3[:len(out3) - 1] 
    else:
        list1 = raw_input().split(" ")
        list2 = raw_input().split(" ")
        raw_input()
        
        for i in xrange(len(list1)):

            for j in xrange(len(letters1)):
                if (list1[i] == letters1[j] and
                    list2[i] == letters2[j]):
                    result += str(j)
        print result


    total = raw_input() 




