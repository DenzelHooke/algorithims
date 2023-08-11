def selectionSort(array):
    lowest_index = 0
    array_length = len(array)

    for i in range(0, array_length-1):
        lowest_index = i
        print('i: ', i)

        for j in range(i+1, array_length):
            print('j:', j)
            if array[j] < array[lowest_index]:
                lowest_index = j
                print('lowest set: ', lowest_index)

        if lowest_index == i:
            continue
        
        # Else
        temp = array[i]
        array[i] = array[lowest_index]
        array[lowest_index] = temp
        print('array: ', array) 
        # print(array)

    
    return array

values = [
    2, 6, 1
]

sorted = selectionSort(values)

print(sorted)   

def selectionSort(array):
    for i in range(0, len(array)-1):
        lowest = i
        
        for p in range(i+1, len(array)):
            if array[p] < array[lowest]:
                lowest = p
        

        temp