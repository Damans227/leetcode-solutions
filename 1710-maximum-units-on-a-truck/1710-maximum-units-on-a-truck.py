class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        maxUnits=0
        
        # [[5,10],[2,5],[4,7],[3,9]]
        # After Sorting 
        # [[5,10],[3,9],[4,7],[2,5]]
        
        boxTypes.sort(key=lambda box: box[1],reverse=True)
        
        for numboxes, unit in boxTypes:
            if truckSize <=numboxes:
                maxUnits += truckSize*unit
                break
            maxUnits += numboxes * unit
            truckSize -= numboxes
        return maxUnits
        