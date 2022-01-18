class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1, s2 = "", ""
        
        for i in word1: 
            s1 = s1+i #String 1 creation
        for j in word2: 
            s2 = s2+j #String 2 creation
            
        if s1 == s2:  #Checking equivallency
            return True
        else:
            return False