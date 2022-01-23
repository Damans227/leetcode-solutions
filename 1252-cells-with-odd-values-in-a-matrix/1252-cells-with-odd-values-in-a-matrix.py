class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        ###### KNOWN ######
        
#        indices[i]=[[r0,c0],[r1,c1]...[ri,ci]]
        
       ###### UNKNOWN #####
#         matrix = m x n, initialized to all 0s

        r = [0]*m
        c = [0]*n
         
#         Increment all the cells on row ri & Increment all the cells on column ci.

        for ri,ci in indices:
            r[ri] +=1
            c[ci] +=1            
        
        ##### FIND #####     
        
        res = 0
        for i in range(m):
            for j in range(n):
                if (r[i]+c[j])%2 ==1:
                    res +=1
        
#         return the number of odd-valued cells in the matrix after applying 
#         the increment to all locations in indices

        return res
