import math


class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        disBetween = maxDis = 0
        
        # case1: distance between two 1. like [1, 0, 0, 0, 1, 0, 1]
        for i in range(len(seats)):
            if seats[i] == 1:
                disBetween = 0
            else:
                disBetween += 1
                maxDis = max(maxDis, math.ceil(disBetween / 2))


        # case2: place alex at left most position. like: [0, 0, 0, 1]
        for i in range(len(seats)):
            if seats[i] == 1:
                maxDis = max(maxDis, i)
                break
    
        # case3: place alex at right most position. like: [1, 0, 0, 0]
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                maxDis = max(maxDis, len(seats) - 1 - i)
                break

        return maxDis