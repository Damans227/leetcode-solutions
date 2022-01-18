class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max=0
        for sentence in sentences:
            num=len(sentence.split(" ")) #Split a string into a list where each word is a list item
            if num > max:
                max = num
        return max