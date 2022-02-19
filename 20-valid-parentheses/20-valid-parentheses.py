class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpen = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in closeToOpen.values():
                stack.append(char)
            elif char in closeToOpen.keys():
                if stack == [] or closeToOpen[char] != stack.pop():
                    return False
                
        return stack == []