class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        
        for i in nums:
            cnt=0
            for j in nums:
                if i > j:
                    cnt+=1
            res.append(cnt)
        return res
    
 #Optimized solution using hashmap to store the index position of sorted list, which itself gives the freq of smaller numbers  
#     	temp = sorted(nums)
# 	    mapping = {}
# 	    result = []
# 	    for i in range(len(temp)):
# 	    	if temp[i] not in mapping:
# 	    		mapping[temp[i]] = i
# 	    for i in range(len(nums)):
# 	    	result.append(mapping[nums[i]])
# 	    return result