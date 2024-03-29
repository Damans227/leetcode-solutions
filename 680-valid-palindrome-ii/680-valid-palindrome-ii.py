class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check_palindrome(i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if check_palindrome(i+1, j) or check_palindrome(i, j-1):
                    return True
                else:
                    return False
        return True