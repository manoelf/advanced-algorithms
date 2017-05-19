#https://www.hackerrank.com/contests/basico-2017-1-lista-2/challenges/camelcase


def count_upper_case(string):
    result = 0
    for i in xrange(len(sequence)):
        if (sequence[i] == sequence[i].upper()):
            result += 1
    return result


sequence = raw_input()

result =  count_upper_case(sequence) + 1 #That one will be the first word

print result
