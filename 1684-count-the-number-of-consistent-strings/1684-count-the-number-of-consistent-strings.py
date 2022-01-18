class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        inconsistentWordCount = 0
       
    #Find the inconsistent word count and substract that from the words list to get consistent wordCount
        for word in words:
            for letter in word:
                if letter not in allowed:
                    inconsistentWordCount += 1
                    break
        
        return len(words) - inconsistentWordCount