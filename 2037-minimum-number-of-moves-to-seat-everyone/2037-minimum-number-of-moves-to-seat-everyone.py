class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        
        zipped_list=zip(seats, students)
        differ=[]
        
        for i,j in zipped_list:
            differ.append(abs(i-j))
        
        return sum(differ)