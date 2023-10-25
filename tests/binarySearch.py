class BinarySearch:
    # Conditions:
    # Array must be sorted prior
    # O(log2 N)

    def __init__(self, array):
        self.array = array

    
    def sort(self, search_value):
        lower = 0
        upper = len(self.array)-1

        while lower <= upper:
            midpoint = (lower+upper) // 2
            midpoint_value = self.array[midpoint]

            if midpoint_value == search_value:
                return midpoint
            
            if midpoint_value < search_value:
                lower = midpoint+1

            if midpoint_value > search_value:
                upper = midpoint-1
        
        return -1
        

value = BinarySearch([3, 6, 8, 10, 12]).sort(3)

print(value)