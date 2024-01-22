values = [9, 8, 7, 6, 5, 4, 3, 2, 1]


# def bubbleSort(arr):
#     print(len(arr))
#     sort_until_index = len(arr)-1
#     sorted = False
#     steps = 0
#     while not sorted:
#         steps += 1
#         sorted = True

#         for i in range(0, sort_until_index):
#             steps += 1
#             if arr[i] > arr[i+1]:
#                 steps += 1
#                 sorted = False
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#         sort_until_index -= 1
#     print(steps)
#     return arr




# O(n^2) Run time
def bubbleSort(arr): 
    sorted_until = len(arr)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, sorted_until):
            # Make Swap
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]          

                sorted = False       
        # Shorten length by 1
        sorted_until -= 1
    
    return arr

    
        








result = bubbleSort(values)

print(result)
