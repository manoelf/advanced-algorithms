#https://www.urionlinejudge.com.br/judge/pt/problems/view/1068

while (True):
    try:
        parenteses = []
        equation = raw_input()
        result = "correct"
        for i in equation:
            if (i == "("):
                parenteses.append(i)
            elif (i == ")" and len(parenteses) != 0):
                parenteses.pop()
            elif(i == ")" and len(parenteses) == 0):
                result = "incorrect"
                break

        if (result != "incorrect" and len(parenteses) != 0):
            result = "incorrect"
    
        print result

    except:
        break
