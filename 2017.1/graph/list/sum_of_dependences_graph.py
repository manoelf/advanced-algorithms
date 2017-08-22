#http://practice.geeksforgeeks.org/problems/sum-of-dependencies-in-a-graph/0

def generate_graph(array, size):
    dic = {}
    for i in range(0, size, 2):
        if (array[i] in dic):
            dic[array[i]].append(array[i + 1])
        else:
            dic[array[i]] = [array[i + 1]]
    return dic

def cont_dep(dic):
    result = 0
    for i in dic:
        result += len(dic[i])
    return result
    
    

tests = int(raw_input())

for i in xrange(tests):
    vertex, edge = raw_input().split()
    array = raw_input().split()
    dic = generate_graph(array, 2 * int(edge))
    result = cont_dep(dic)
    print result

       
    








