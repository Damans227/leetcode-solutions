class Solution:
    def replaceDigits(self, s: str) -> str:
        
        ##### Known #####
        # s = "a1c1e1 i.e, lowercase english letter in EVEN and digits in ODD
        
        res=""
        ##### UnKnown #####
        
        # shift(c,x) returns xth character after c
        
        def shift(self, c, x):
            return chr(ord(c)+int(x))
        
        ##### Find #####
        
        # s after replacing all the digits on its ODD places with shift(s[i-1], s[i])
        for i in range(0, len(s)):
            
            if i % 2 != 0:
                res += shift(self, s[i-1], s[i])
                continue
            
            res +=s[i]
        
        return res