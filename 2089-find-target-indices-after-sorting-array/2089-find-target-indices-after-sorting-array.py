class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        targetList=[]
        for index, num in enumerate(nums): #enumerate will return index and the corresponding number from nums
            if(num==target):
                targetList.append(index)
        return targetList
                