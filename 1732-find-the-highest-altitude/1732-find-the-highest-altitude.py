class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        ############ Known ############ 

        # Road trip 0,1,2....n+1 Points
        
        # altitude at point 0, is 0        
        
        # gain=[1,2,3...i] netGain in altitude = gain[i]
        
        # gain = [-5,1,5,0,-7]
        
        ############ What we dont know:############
        
        # To find the highest altitude we need to find altitudes at all points, we only the know the altitude at point 0
        
        altitudes=[0]
        i=0
        for netGain in gain:
            altitude=netGain+altitudes[i]
            i+=1
            altitudes.append(altitude)
        
        ############ Find highest altitude ############

        return max(altitudes)