class Solution:
    def firstUniqChar(self, s: str) -> int:
        strLength=len(s)
        d={}
        for ch in s: # Map the frequency of each character in a dictionary 
            if ch not in d:
                d[ch]=1
            else:
                d[ch]-=1
        
        i=strLength
        
        for key in d.keys(): # Parse through all the keys, and find one with the smallest index
            if d[key] > 0:
                i=min(s.index(key),i)
            
        return -1 if i == strLength else i 