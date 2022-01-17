class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        
        zipped_list=list(zip(seats, students))
        differ=[]
        
        for t in zipped_list:
            i,j=t
            differ.append(abs(i-j))
        
        return sum(differ)