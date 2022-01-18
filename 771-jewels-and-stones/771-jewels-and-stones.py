class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d={}
        charToFreqS = {}  # Map character to its frequency in S.
        numJewels = 0  # Total number of jewels.
        
        for stone in stones:
            if stone not in charToFreqS:
                charToFreqS[stone] = 1
            else:
                charToFreqS[stone] += 1
        
        for jewel in jewels:
            if jewel in charToFreqS:
                numJewels += charToFreqS[jewel]
                
        return numJewels