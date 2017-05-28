


def my_split(numbers, result):
    num = ""
    for i in numbers:
        if (i != " "):
            num += i 
        else:
            result.append(int(num))
            num = ""
    result.append(int(num))


a = "1 2 3 4 -5 6"
b = []
my_split(a, b)
print b
