import string



# Hash Maps
# pg 131

# Write a function that returns the values of 2 intersection arrays. Should be o(n).

def findIntersectionHash(arr1, arr2):

    smallerArray = []
    largerArray = []
    hashMap = {}
    intersectingValues = []
    steps = 0
    

    # Creates hash map of all items in larger array to compare against
    # O(n)
    for item in arr1:
        steps += 1
        if not item in hashMap:
            hashMap[item] = True

    # O(n)
    for item in arr2:
        steps += 1
        if item in hashMap:
            intersectingValues.append(item)


    print("O(n): ", intersectingValues)
    print("Steps: ", steps)




def findIntersection(arr1, arr2):
    smallerArray = []
    largerArray = []
    intersectingValues = []
    steps = 0

    if(arr1 > arr2):
        smallerArray = arr2
        largerArray = arr1
    else:
        smallerArray = arr1
        largerArray = arr2

    # O(n^2) Quadratic
    for i in smallerArray:
        steps += 1
        for x in largerArray:
            steps += 1
            if x == i:
                intersectingValues.append(x)
    
    print("O(n^2): ", intersectingValues)
    print("Steps: ", steps)

    

# array1 = [
#     9 ,12, 1, 0, 9 ,12, 1, 0, 9 ,12, 1, 0, 9 ,12, 1, 0,9 ,12, 1, 0,9 ,12, 1, 0
# ]
# array2 = [
#     9, 2, 0, 6, 4
# ]




# findIntersection(array1, array2)
# findIntersectionHash(array1, array2)


# Create a function that returns the first duplicate string within 1 array

# O(n)
def findDuplicateString(arr):

    hashMap ={}

    for i in arr:
        if not i in hashMap:
            hashMap[i] = True
            continue


        print("Duplicate: ", i)
        return

# findDuplicateString(['c', 'b', 'c', 'd', 'f'])


# A function that accepts a string that includes all leters of the alphabet except one. Return the missing letter.

# O(n+26) -> o(n) (Drop constants)
def findMissingLetter(string):
    print(len(string))
    hashMap = {
        'a': False, 'b': False, 'c': False, 'd': False, 'e': False,
        'f': False, 'g': False, 'h': False, 'i': False, 'j': False,
        'k': False, 'l': False, 'm': False, 'n': False, 'o': False,
        'p': False, 'q': False, 'r': False, 's': False, 't': False,
        'u': False, 'v': False, 'w': False, 'x': False, 'y': False, 'z': False
    }
    count = 0
    
    for char in string:
        count += 1
        hashMap[char] = True

    for i in hashMap.keys():
        count += 1
        if hashMap[i] == False:
            print(i)
    print(count)

    print(hashMap.values())

# o(n) My version
def findFirstDuplicate(string):
    hashTable = {}
    

    for i in string:
        if not i in hashTable:
            hashTable[i] = False
        else:
            hashTable[i] = True
        
    for key, value in hashTable.items():
        if value == True:
            print(key)
            return

def findFirstNonDuplicateSolved(string):

    hashTable = {}


    for i in string:
        if i in hashTable:
            hashTable[i] += 1
            continue
        hashTable[i] = 1
    
    for x in string:
        if hashTable[x] == 1:
            print(x)
            return
        
    


            
            
        
    


# findFirstDuplicate('juumboj')
# findFirstNonDuplicateSolved('juummmmmboj')



    



# findMissingLetter('the quick brown fox jumps over the lazy bog')


# Ch 9 
# 4.


class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def read(self):
        return self.data[-1] or False
    
    def is_empty(self):
        if len(self.data) > 0:
            return False
        return True
    
class Reverser:
    def __init__(self):
        self.stack = Stack()

    
    def reverse(self, string):
        reversedString = ''

        for char in string:
            self.stack.push(char)
        
        while not self.stack.is_empty():
            reversedString += self.stack.pop()
            

        
        print(reversedString)


if __name__ == "__main__":
    Reverser().reverse('abcde')        












        
        
