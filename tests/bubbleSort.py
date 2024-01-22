class BubbleSort:
    # Conditions:
    # N/A
    # O(N^2)

    def __init__(self, array):
        self.array = array

    
    def sort(self):
        sorted = False
        sort_until = len(self.array)-1
        steps = 0

        while not sorted:
            sorted = True

            for i in range(0, sort_until):
                steps += 1
                if self.array[i] > self.array[i+1]:
                    steps += 1
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
                    sorted = False
            
            sort_until -= 1
        
        print(steps)
        return self.array

value = BubbleSort([5, 3, 1, 2]).sort()

print(value)