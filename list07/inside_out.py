#https://www.urionlinejudge.com.br/judge/pt/problems/view/1235

def reverse_inside_out(line):
    first_part = ''
    second_part = ''
    size = len(line)
    for i in xrange(size):
        if (i > size/2 - 1):
            first_part += line[size - i - 1]
        else:
            second_part += line[size - i -1]
    print first_part + second_part

n = int(raw_input())
for i in xrange(n):
    line = raw_input()
    reverse_inside_out(line)




