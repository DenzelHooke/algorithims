values = [
    1334, 2, 1, 99
]

# def binary_search(arr, search_value):
#     lower_bound = 0
#     upper_bound = len(arr)-1

#     while lower_bound <= upper_bound:
#         # Midpoint integer
#         midpoint = (lower_bound + upper_bound) // 2
#         midpoint_value = arr[midpoint]

#         if midpoint_value == search_value:
#             return midpoint

#         elif search_value > midpoint_value:
#             lower_bound = midpoint+1
        
#         elif search_value < midpoint_value:
#             upper_bound = midpoint-1
    
#     return -1

def binary_search(arr, search_val):
    lower = 0
    upper = len(arr)-1

    while lower <= upper:
        midpoint = (lower + upper) // 2
        midpoint_val = arr[midpoint]

        if midpoint_val == search_val:
            return midpoint

        elif midpoint_val > search_val:
            upper = midpoint-1

        elif midpoint_val < search_val:
            lower = midpoint_val+1


    return -1     

def bblSort(arr):
    sort_until = len(arr)-1
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, sort_until):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
        sort_until =- 1
    
    return arr


bblSorted = bblSort(values)
found = binary_search(values, 1334)
print(found)
