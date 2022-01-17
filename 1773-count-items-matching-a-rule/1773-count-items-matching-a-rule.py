class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0 # Setup a count variable
         
        for item in items: #Parse through every single item inside the items list
            if(ruleKey=="type"): # Check for a matching ruleKey
                if(item[0]==ruleValue):
                    count +=1 #Increase the count if a match is found
            elif(ruleKey=="color"):
                if(item[1]==ruleValue):
                    count +=1
            else:
                if(item[2]==ruleValue):
                    count+=1
        
        return count
   
    # Optimized solution using a HashMap/ Dictionary. 
    
    # rule = {'type' : 0, 'color' : 1, 'name' : 2}
    # def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    #     cnt, index = 0, self.rule[ruleKey]
    #     for item in items:
    #         if item[index] == ruleValue:
    #             cnt += 1
    #     return cnt
                
                