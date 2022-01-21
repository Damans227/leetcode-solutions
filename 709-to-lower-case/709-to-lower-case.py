class Solution:
    def toLowerCase(self, s: str) -> str:
        res=""
        #Convert each char to ASCII value. For any Uppercase ASCII value add 32 to it for its lowercase value
        for ch in s:
            if ord(ch) > 64 and ord(ch) < 91:
                res+=chr(ord(ch)+32)
            else:
                res+=ch
        return res