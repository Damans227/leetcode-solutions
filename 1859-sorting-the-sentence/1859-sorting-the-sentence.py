class Solution:
    def sortSentence(self, s: str) -> str:
        listOfWords = s.split(" ")
        originalList=[None]*len(listOfWords)
        originalSentence=" "
        for word in listOfWords:
            originalList[int(word[-1])-1]=word[:len(word)-1]
        
        return originalSentence.join(originalList)