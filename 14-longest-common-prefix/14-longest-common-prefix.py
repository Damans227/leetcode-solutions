class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
               
        longestCommonPrefix = "";
        if(strs == None or len(strs) == 0):
            return longestCommonPrefix       

        index = 0 # 1) Select item on each index and verify it against same indexed item of first string
        for c in strs[0]: 
            for i in range(1, len(strs)): #2) Do 1 for all indexes
                if(index >= len(strs[i]) or c!= strs[i][index]):    
                    return longestCommonPrefix
                
            longestCommonPrefix += c
            index+=1

        return longestCommonPrefix
