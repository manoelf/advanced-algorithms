min_diff = {}

def find_min_diff(array, n):
    mini = float("inf")
    for i in xrange(n - 1):
        aux = abs(array[i] - array[i+1])
        if (not(min_diff.has_key(aux))):
            min_diff[aux] = []
        if (aux < mini):
            mini = aux
        min_diff[aux].append(array[i])
        min_diff[aux].append(array[i+1])
        
    return mini

n = int(raw_input())
array = map(int, raw_input().split())

array.sort()
result = find_min_diff(array, n)

answer = min_diff[result]


for i in answer:
    print i,
