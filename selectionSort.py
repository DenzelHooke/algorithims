values = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def selectionSort(arr):
    length_until_sorted = len(arr) -1
    for i in range(0, length_until_sorted):
        lowestNumberIndex = i

        for x in range(1, length_until_sorted+1):
            if(arr[x] < arr[lowestNumberIndex]):
                lowestNumberIndex = x

        if lowestNumberIndex != i:
            temp = arr[i]
            arr[i] = arr[lowestNumberIndex]
            arr[lowestNumberIndex] = arr[i]

    print(arr)

selectionSort(values)

        
                