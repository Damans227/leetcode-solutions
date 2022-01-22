class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        ######## Known ###########
        
        # Array of rectangles, where rectangle[i]=[length of i, width of i]
    
        # rectangles = [[5,8],[3,9],[5,12],[16,5]]
        
        ######## Unknown ##########
        
        # Transform rectangle[i] to square[i] of side length k <= length of i < width of i
        #  maxLen -> side length of largest square
        
        maxLen=0
        count=0
        
        for rectangle in rectangles:
            if(min(rectangle) > maxLen): 
                maxLen=min(rectangle)
        
        
        ######### Find ############
        
        # number of rectangles which can form square of side length maxLen
        for rectangle in rectangles:
            if min(rectangle) == maxLen:
                count+=1
                
        return count