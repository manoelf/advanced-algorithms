#https://www.urionlinejudge.com.br/judge/pt/problems/view/1426

n = int(raw_input())

def fill_first(a1, a3):
    new = []
    for i in xrange(5):
        new.append(a1[i])
        if (i < 4):
            new.append((a3[i] - (a1[i] + a1[i + 1]))/2)
    return new

def print_matrix(matrix):
    out = ""
    for i in range(8, -1, -1):
        part = ""
        for j in range(len(matrix[i])):
            part += str(matrix[i][j]) + " "
        out += part[0:len(part) - 1] + "\n"
    print out[0:len(out)-1]

def fill_matrix(matrix):
    new_matrix = []
    new_matrix.append(matrix[8])
    for i in xrange(8):
        line = []
        for j in xrange(len(new_matrix[i]) - 1):
            line.append(new_matrix[i][j] + new_matrix[i][j+1])
        new_matrix.append(line)
    return print_matrix(new_matrix)




matrix = []
newMatrix = []

for i in xrange(n):
    matrix = []
    new_matrix = []

    for i in xrange(5):
        array = map(int, raw_input().split())
        matrix.append(array)
        matrix.append([])
    matrix[8] = fill_first(matrix[8], matrix[6])

    fill_matrix(matrix)
    

    






