#http://practice.geeksforgeeks.org/problems/count-all-possible-paths-from-top-left-to-bottom-right/0
def fill(a, i, j):
    if (i == 0 or j == 0):
        a[i][j] = 1
    else:
        a[i][j] = a[i][j-1] + a[i-1][j]

def full_fill(row, col):
    array = []
    array = [[0 for i in range(col)] for j in range(row)]
    for i in xrange(row):
        for j in xrange(col):
            fill(array, i, j)
    return array[row - 1][col - 1]

t = int(raw_input())
for i in xrange(t):
    row, col = map(int, raw_input().split())
    print full_fill(row, col)
   
