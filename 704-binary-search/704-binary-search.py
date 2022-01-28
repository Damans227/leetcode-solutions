class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        p, q = 0, len(nums)-1
        
        while(p<=q):
            index=int((p+q)+1/2)
            find=nums[index]
            if(find==target):
                return index
            else:
                if(find<target):
                    p=index+1
                else:
                    q=index-1
        return -1
    
