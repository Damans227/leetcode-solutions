class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        #brute force way O(s+t)
        sMap = {}
        tMap = {}
        
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)

        # return Counter(s) == Counter(t)

        for k in sMap:
            if sMap[k] != tMap.get(k,0):
                return False
        return True