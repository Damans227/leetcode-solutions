class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [2,7,11,15], target = 9
        # O(n^2) Solution
        # for i in range(0,len(nums)): # Use this for loop to select num1
        #     num1=nums[i]
        #     for j in range(i+1, len(nums)): # Use this for loop to select num2
        #         complement=target-num1
        #         if (nums[j]==complement):
        #             return [i,j]
        # return []
        
        #O(n) Solution
        hashMap={}
        for i, n in enumerate(nums):
            check=target-n
            if check not in hashMap:
                hashMap[n]=i
            else:
                return [hashMap[check],i]
        return