class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        finger = 0 #Set finger at 0
        res=[] # An array to store all the distances
        for letter in word: #Parse through every single letter
            pos = keyboard.find(letter) #Find position of the letter on keyboard
            dist = pos - finger #Find the disatnce between finger and letter position
            res.append(abs(dist)) 
            finger=pos #Update the finger position
        return sum(res) #Sum all distances
        
        
        