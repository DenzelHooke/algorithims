values = [1,100, 400, 4, 5, 2, 9]



def greatestNumber(array):
    value = 0
    for i in array:
        if i > value:
            value = i

    print(value)

greatestNumber(values)