class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
       
    #Map each integer and its frequency in a dictionary. Then parse through the dictionary to find out which
    #integer occurs exactly 3 times. That integer is the one which is common between all 3 lists. 
       
        hashMap={}  
        GiantList=arr1+arr2+arr3
        res=[]
        
        for i in GiantList:
            if(i not in hashMap):
                hashMap[i]=1
            else:
                hashMap[i]+=1
        
        for i in hashMap:
            if(hashMap[i]==3):
                res.append(i)
        
        return res
            
        