class SelectionSort:
    # Conditions:
    # N/A
    # O(N^2)

    def __init__(self, array):
        self.array = array

    
    def sort(self):
        steps = 0
        for i in range(len(self.array)):
            min_index = i

            for x in range(i+1, len(self.array)):

                steps += 1
                if(self.array[x] < self.array[min_index]):
                    min_index = x
                    

            steps += 1
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            
        print(steps)
        return self.array

value = SelectionSort([5, 3, 1, 2]).sort()

print(value)