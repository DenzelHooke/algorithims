# def reverseStr(string):
    
#     if len(string) == 1:
#         return string[0]
    
#     return reverseStr(string[1:]) + string[0]


# # a = reverseStr('abc')

# # print(a)


# # countX

# 'axbxdxc'

# def countX(string, count=0):
#     if len(string) == 1:
#         return count

#     if string[0] == 'x':
#         count += 1
#         return countX(string[1:], count)
    
#     return countX(string[1:], count)

# a = countX('axbxdxc')

# print(a)

# # Staircase

# def num_of_paths(n):

#     if n <= 0:
#         return 0
    
#     elif n == 1:
#         return 1
    
#     elif n == 2:
#         return 2
    
#     elif n == 3:
#         return 4
        
#     return num_of_paths(n-1) + num_of_paths(n-2) + num_of_paths(n-3)

# b = num_of_paths(6)

# print(b)

# Remove Duplicates from Sorted Array (leetcode)



# O(n + n) = O(n)
# def removeDuplicatesSorted(array):
    
#     hashMap = {}
#     totalSize = len(array)
#     count = 0
    
#     for i,v in enumerate(array):
#         if v not in hashMap:
#             hashMap[v] = v
#         array[i] = "_"
            
#     # Rebuild inplace
#     for key, value in hashMap.items():
#         array[count] = hashMap[key]
#         count += 1
        
#     while True:
#         if array[-1] == "_":
#             array.pop()
#             continue
        
#         break
        
#     print(array, len(hashMap))
        
    
    
# removeDuplicatesSorted(nums)
nums = [0,0,0,0,1,1,1,2,2,3,3,4]
def removeDuplicatesSortedPointer(nums):
    hashMap = {}
    left = 0
    right = 1
    
    while True:
        
        if nums[left] == nums[right]:
            right += 1
            continue
            
        hashMap[nums[left]] = True
        left += 1

# removeDuplicatesSortedPointer(nums)

# print(nums)
            
# count = 0;

# pastProblems 

# def numOfStairs(n):
#     global count
#     global pastProblems
    
#     count += 1
    
#     if n in pastProblems:
#         return pastProblems[n]
    
    
#     if n <= 0:
#         return 0
    
#     elif n == 1:
#         return 1
    
#     elif n==2:
#         return 2
    
#     elif n==3:
#         return 4

    
#     result = numOfStairs(n-1) + numOfStairs(n-2) + numOfStairs(n-3)
    
#     pastProblems[n] = result
    
#     return result 

# a = numOfStairs(10)

# print(a)
# print(count)
# print(pastProblems)

# ["ab", "cd", "e"]

# def countChars(array):
    
#     if len(array) <= 1:
#         return len(array[0])

    
#     return len(array[0]) + countChars(array[1:])

# b = countChars(["ab", "cd", "e"])

# def evenNums(array, newArray):
#     if array[0] % 2 == 0:
#         newArray.append(array[0])
    
#     if len(array) <= 1:
#         return newArray        
    
    
#     return evenNums(array[1:], newArray)

# a = evenNums([1, 2, 3, 4, 5, 6, 12, 20, 10], [])

# print(a)

# def trianglePattern(n):
#     if n == 1:
#         return 1
    
#     return n + trianglePattern(n-1)

# a = trianglePattern(3)

# print(a)

# def findX(string, index=0):
#     print(string)
#     if string[0] == "x":
#         return index
    
#     return findX(string[1:], index+1)   

# a = findX("abcdefghijklmnopqrstuvwxyz") 

# print(a)2

# Max number

def maxOfArray(array):
    print("recursion")
    
    if len(array) == 1:
        return array[0]
    
    max_remainder = maxOfArray(array[1:])
    

    if array[0] > max_remainder:
        return array[0]
    
    return max_remainder

def maxOfArray2(array):
    print("recursion")
    
    if len(array) == 1:
        return array[0]
    
    maxRemainder = maxOfArray2(array[1:])
    
    if array[0] > maxRemainder:
        return array[0]
    else:
        return maxRemainder
    
    
    
    
    return max_remainder


# a = maxOfArray([1,2,3,4,5,6])
b = maxOfArray2([1,2,3,4,5,6]) 