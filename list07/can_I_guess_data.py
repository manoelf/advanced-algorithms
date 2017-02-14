#https://www.urionlinejudge.com.br/judge/pt/problems/view/1340


while (True):
    try:
        n = int(raw_input())

        add = []
        remove = []

        stack = True
        queue = True
        priority = True


        for i in xrange(n):
            operation, num = map(int, raw_input().split())
            if (operation == 1):
                add.append(num)
            else:
                remove.append(num)
                

        for i in xrange(len(remove)):
            if (remove[i] != add[i] and queue):
                queue = False
            if (remove[i] != add[len(remove) - 1 - i] and stack):
                stack = False 
            if (i > 0):
                if (remove[i] >  remove[i - 1] and priority):
                    priority = False

        if (n <= 2):
            priority = False
        if (not(stack) and not(queue) and not(priority)):
            print "inpossible"
        elif ((stack and queue) or (stack and priority) or (queue and priority)):
            print "not sure"
        elif (queue):
            print "queue"
        elif (stack):
            print "stack"
        elif (priority):
            print "priority queue"

    except:
        break
    

