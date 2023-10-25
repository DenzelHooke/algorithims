class SelectionSort:
    # Conditions:
    # N/A
    # O(N^2)

    def __init__(self, array):
        self.array = array

    
    def sort(self):
        for i in range(len(self.array)):
            min_index = i
            min_value = self.array[min_index]

            for x in range(i+1, len(self.array)):
                if(self.array[x] < min_value):
                    min_index = x
                    # min_value = self.array[x] 


            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            
                
        return self.array

value = SelectionSort([5, 3, 1, 2]).sort()

print(value)