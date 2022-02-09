from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # using Kahn's Algorithm in “Topological sorting”
        result = [0] * numCourses
        if numCourses == 0:
            return result

        if not prerequisites:
            result = [i for i in range(numCourses)]      
            return result

        in_degree = [0] * numCourses
        zero_degree = deque()
        adjacency_list = {}

        # build adjacency list to track neighbors
        # and update in_degree(number of dependent nodes) array
        for pre in prerequisites:
            in_degree[pre[0]] += 1
            if pre[1] in adjacency_list:
                adjacency_list[pre[1]].append(pre[0])
            else:
                adjacency_list[pre[1]] = [pre[0]]
        
        # append the node in the queue which does not have any dependency
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                zero_degree.append(i)

        if len(zero_degree) == 0:
            return []

        # pop from the queue and go to it's all neigbors to decrease their depedency number from 'in_degree' array
        index = 0
        while zero_degree:
            course = zero_degree.popleft()
            result[index] = course
            index += 1

            if course in adjacency_list:
                for neighbor in adjacency_list[course]:
                    in_degree[neighbor] -= 1
                    # if no dencey of the neighbor then add to the queue
                    if in_degree[neighbor] == 0:
                        zero_degree.append(neighbor)

        # check all node presents in the result array
        if index < numCourses-1:
            return []

        return result