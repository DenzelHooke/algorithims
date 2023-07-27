values = [
1, 5, 7, 10, 14, 20,    
]


def binary_search(arr, search_value):
    length = len(arr)
    upper = length-1
    lower = 0

    while lower <= upper:
        midpoint = (upper + lower) // 2
        midpoint_value = arr[midpoint]

        if midpoint_value == search_value:
            return midpoint_value
        
        elif search_value < midpoint_value:
  
            upper = midpoint -1
        elif search_value > midpoint_value:
            lower = midpoint +1

    
    return -1

binary_search(values, 6)