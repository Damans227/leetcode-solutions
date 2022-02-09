class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr: 
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        valueSet = set(d.values())
        
        if(len(valueSet) < len(d)):
            return False
        else:
            return True
        