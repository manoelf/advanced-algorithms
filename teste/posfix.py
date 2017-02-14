#https://www.urionlinejudge.com.br/judge/pt/problems/view/1077

operators = "*/+-^"
expression = "((a*b)-(d*f))/(j*k)"

def posfix()
oper_aux = ""
numbers = ""
start = False
result = ""
for i in xrange(len(expression)):
    if (expression[i] == "("):
        start = True
    elif (expression[i] == ")"):
        result += numbers + oper_aux
        oper_aux = ""
        numbers = ""
        start = False
    elif (expression[i] in operators):
        oper_aux += expression[i]
    else:
        numbers += expression[i]
print result
