class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #brute force way O(s+t)
        sMap = {}
        tMap = {}
        
        
        #O(s)
        for c in s:
            sMap[c] = 1 + sMap.get(c, 0)
        #O(t)
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)

        for k in sMap.keys():
            if((k not in tMap) or (len(sMap)!=len(tMap)) or sMap[k]!=tMap[k]):
                return False
        return True