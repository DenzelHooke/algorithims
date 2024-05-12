class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}          
        
        
        for i, x in enumerate(nums):
            diff = target - x

            if diff in hashMap:
                print([hashMap[target - x], i])
                return
            
            hashMap[x] = i

        return
    

    def twoSumBrute(self, nums: list[int], target: int) -> list[int]:
        index = 0
        
        while index < len(nums):
            for x in range(index+1, len(nums)):
                if nums[index] + nums[x] == target:
                    return [index, x]

            index += 1
        return None
            


Solution().twoSum([1, 3, 5, 7], 6)
# Solution().twoSumBrute([3,2,4], 6)