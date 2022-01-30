class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        setOfNums = set(nums)
        length1=len(nums)
        length2=len(setOfNums)
        
        if length1 == length2:
            return False
        else:
            return True