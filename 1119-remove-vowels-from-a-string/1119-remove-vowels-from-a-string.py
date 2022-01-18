class Solution:
    def removeVowels(self, s: str) -> str:
        
        vowels=['a','e','i','o','u']
        for v in vowels:
            s = s.replace(v,'') #string replace method: https://www.w3schools.com/python/ref_string_replace.asp
        return s
    
    #Solution without using in-built method repalce. 
    
    # class Solution:
    # def removeVowels(self, S: str) -> str:
    #     s = set('aeiou')
    #     ret = ""
    #     for ch in S:
    #         if ch not in s:
    #             ret += ch
    #     return ret
