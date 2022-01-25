class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum=nums[0]
        curSum=0
        
        #Move to the next element in the array, and decide whether you want 
        #to start a new subarray or continue the previous subarray by 
        #comparing the MaxSum and curSum. 
        
        for n in nums:           
            curSum = max(n+curSum, n) #Should I start a new subarray ? 
            maxSum = max(maxSum, curSum)
        return maxSum