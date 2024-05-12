# arrs = [
# ['Dir1', 'Dir2', ['Dir3', ['Dir4', ['Dir 5', ['Dir 6', ['Dir 7']]]]], ['Dir 8']]
# ]

# count = 0

# def reccursiveSearch(arr):
#     global count
    
#     for element in arr:
#         count += 1
        
#         if isinstance(element, list):
#             reccursiveSearch(element)
#             continue
#         print(element)
        

# reccursiveSearch(arrs)
# print(count)


# def doubleArray(arr, index):
#     # Base Case
#     if index >= len(arr):
#         return
    
#     arr[index] *= 2
#     doubleArray(arr, index+1)
    
# x = [1, 2, 3, 4, 5]

# doubleArray(x, 0)

# print(x)

# arr = [1, 2, 3, 4, 5]

# def countAll(array):
    
#     if len(array) == 1:
#         return array[0]
     
#     return array[0] + countAll(array[1:])


# def reverseString(string):
    
#     if len(string) == 1:
#         return string[0]
    
#     return string[-1] + reverseString(string[0: -1])



# a = reverseString("457847892902ru9djo2douj2d9u2d")

# # (O(n`    c9oiioi99o087u  `))
# def countX(string):
    
#     # Base case
#     if len(string) == 0:
#         return ""
    
#     if string[0] == "x":
#         return 1 + countX(string[1:])
    
#     return countX(string[1:])



# # Staircase




# def num_of_steps(n):
#     print(n)

#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
        
    
#     return num_of_steps(n-1) + num_of_steps(n-2) + num_of_steps(n-3)

# a = num_of_steps(4)

# print("end: ", a)

# Anagram finder

# abcd

# abdc
# acbd
# acdb
# adbc
# adcb
# bacd
# badc
# bcad
# bcda
# bdac
# bdca
# cabd
# cadb
# cbad
# cbda
# cdab
# cdba
# dabc
# dacb
# dbac
# dbca
# dcab
# dcba

`
# def arraySearch(array):
    
#     for element in array:
#         if isinstance(element, list):
#             arraySearch(element)
#             continue 
        
#         print(element)

# array = [
#     1, [2, 3, [4, [5, [6]]], 7, 8, [9], 10]
#     ]
# arraySearch(array)


# Top down recurrsion
# def sumAll(arr):
#     if len(arr) == 1:
#         return arr[0]
        
#     return arr[0] + sumAll(arr[1:])

# a = sumAll([10, 10, 1])


# # abc
# def reverseString(string):

#     if len(string) == 1:
#         return string[0]

#     return reverseString(string[1:]) + string[0]
    
    
# a = reverseString("abc")

# print(a)`
    