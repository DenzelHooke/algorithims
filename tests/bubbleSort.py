class BubbleSort:
    # Conditions:
    # Array must be sorted prior

    def __init__(self, array):
        self.array = array

    
    def sort(self):
        sorted = False
        sort_until = len(self.array)-1

        while not sorted:
            sorted = True

            for i in range(0, sort_until):
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
                    sorted = False
            
            sort_until -= 1
        
        return self.array

value = BubbleSort([5, 3, 1, 2, 4]).sort()

print(value)