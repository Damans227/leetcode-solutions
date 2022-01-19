class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        cnt=0
        checker=0
        
        for ch in s:
            if ch=="R":  #For every R we increment checker by 1
                checker+=1
            else:
                checker-=1 #For every L we decrement checker by 1
           
            if checker==0: #When checker is 0, we know we have a balanced substring and we increment the count
                cnt+=1
                
        return cnt