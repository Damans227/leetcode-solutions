class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1
        res=0
        #O(n) solution using 2 pointer
        while(l<r):
            area = (r-l) * min(height[l], height[r])
            res=max(area,res)
            
            if(height[r]>height[l]):
                l+=1
            else:
                r-=1
        return res