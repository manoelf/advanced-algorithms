#https://www.urionlinejudge.com.br/judge/pt/problems/view/1898

cpf = raw_input()
caracteres = raw_input()

cont = 0

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

new_cpf = ""

value1 = ""
value2 = ""
for i in cpf:
    if (i in num):
        if (cont < 11):
            new_cpf += i
        else:
            value1 += i 
        cont += 1
        print i + " " + value1

for i in caracteres:
    if (i in num):
        value2 += i
    print i + " " + value2
sume  =  float(value1) + float(value2)
print "cpf %d" % int(new_cpf)
print "%.2f" % sume 

