values = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def bubbleSort(arr):
    print(len(arr))
    sort_until_index = len(arr)-1
    sorted = False
    steps = 0
    while not sorted:
        steps += 1
        sorted = True

        for i in range(0, sort_until_index):
            steps += 1
            if arr[i] > arr[i+1]:
                steps += 1
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
        sort_until_index -= 1
    print(steps)
    return arr
        
result = bubbleSort(values)

print(result)


