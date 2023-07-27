values = [
    20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
]

def bubbleSort(array):
    unsorted_until_index = len(array)-1
    sorted = False
    comps = 0
    swaps = 0

    while not sorted:
        sorted = True
        for num in range(unsorted_until_index):
            if array[num] > array[num+1]:
                comps += 1
                array[num], array[num+1] = array[num+1], array[num]
                swaps += 1
                sorted = False
                # print(array)
        unsorted_until_index -= 1

    print(swaps+comps)
    return array

def binary_search(array, search_value):
    lower = 0
    upper = len(array)-1
    
    while lower <= upper:
        midpoint = (upper + lower) // 2
        value_midpoint = array[midpoint]

        if search_value == value_midpoint:
            return midpoint
        elif search_value < value_midpoint:
            upper = midpoint - 1
        elif search_value > value_midpoint:
            lower = midpoint + 1
    
    return -1



            
    

new_list = bubbleSort(array=values)
found = binary_search(new_list, 1)
print(new_list)
print(found)