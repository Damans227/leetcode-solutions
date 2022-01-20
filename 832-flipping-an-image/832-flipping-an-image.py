class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        for segment in image:
            res.append(segment[::-1])
            
        
        for i in range(len(res)):
            for j in range(len(res[i])):
                
                if res[i][j] == 1:
                    res[i][j]=0
                else:
                    res[i][j]=1
        return res