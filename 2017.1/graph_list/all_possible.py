def fill(a, i, j):
    if (i == 0 or j == 0):
        a[i][j] = 1
    else:
        a[i][j] = a[i][j-1] + a[i-1][j]

def full_fill(row, col):
    array = []
    array = [[0 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            fill(array, i, j)
    return array[row - 1][col - 1]

t = int(input())
for i in range(t):
    row, col = input().split()
    print("%d" % (full_fill(int(row), int(col)) % (10**9+7)))
