class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        #We initiate a variable to store the output
        distance = 0
#we initialise the start point with the 1st point in the list, so that we can iterate all the points using this variable
        start_point = points[0]
		#for loop to iterate through all the points
        for point in points[1:]:
		#for the logic behind this formuala, see below in this post
            distance += max(abs(start_point[0]-point[0]),abs(start_point[1]-point[1]))
			#we add up the shortest distances between each points to get the shortest traversal distance
            start_point = point
        return distance
    
    #https://leetcode.com/problems/minimum-time-visiting-all-points/discuss/1114113/Python3-solution-with-explaination