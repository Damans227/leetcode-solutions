class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        #Odd length solution
        for i in range(len(s)):
            res = ""
            l,r = i,i
            while l>=0 and r < len(s) and s[l] == s[r]:
                res = s[l:r+1]
                count+=1
                l -= 1
                r += 1
        
        #Even length solution            
        for i in range(len(s)):
            res = ""
            l,r = i,i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                res = s[l:r+1]
                count+=1
                l -= 1
                r += 1
                
        return count