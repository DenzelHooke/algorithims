class InsertionSort:
    # Conditions:
    # N/A
    # O(N^2)

    def __init__(self, array):
        self.array = array

    
    def sort(self):
        for i in range(1, len(self.array)):

            temp = self.array[i]
            position = i-1

            while position >= 0:
                if self.array[position] > temp:
                    self.array[position+1] = self.array[position]  
                    position = position - 1
                else:
                    break
            self.array[position+1] = temp

        return self.array

  

value = InsertionSort([4, 3, 2, 1]).sort()

print(value)