class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l=[]
        for x in range(1,len(arr)+1,2):
            i=x
            j=0
            while(j<=len(arr) and i<=len(arr)):
                l.append(sum(arr[j:i])) #Keep sliding the window of j->i for odd numbers, e.g 1,3,5
                j+=1
                i+=1
        return sum(l)