class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        
        init=0

        while(init<len(nums)):
                     
            i=nums[init]
            j=index[init]
            
            if(j < len(target)):
                temp=target[j:] #Use slicing the list to shift it to the right when an index already exists
                target[j]=i
                target = target[:j+1] + temp
                init+=1
                                   
            else:
                target.append(i)
                init+=1
                
        return target;