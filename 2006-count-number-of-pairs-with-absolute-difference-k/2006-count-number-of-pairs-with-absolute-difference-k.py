class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        i, cnt = 0, 0
        
        for a in range(i,len(nums)): #Use pointer a at the begining of the list to represent i in the pair of (i,j)
            for b in range(a+1, len(nums)): #Use pointer b to scan all the subsequent j's in the pair of (i,j)
                check = nums[a] - nums[b]
                if(abs(check)==k):
                    cnt +=1 #Increase the count as the absolute value of check is equal to the given value of k
        return cnt
                