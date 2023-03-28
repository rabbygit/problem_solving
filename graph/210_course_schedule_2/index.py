from collections import deque, defaultdict
from typing import List


class Solution:

    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        # using Kahn's Algorithm in “Topological sorting”
        q = deque()
        result = []
        in_degree = {}
        adjacency_list = defaultdict(list)
        
        # build adjacency list to track neighbors
        # and update in_degree(number of dependent nodes) array
        for src, des in prerequisites:
            adjacency_list[des].append(src)
            in_degree[des] = in_degree.get(des, 0)
            in_degree[src] = in_degree.get(src, 0) + 1

        # append the node in the queue which does not have any dependency
        for key in range(numCourses):
            if key not in in_degree or in_degree[key] == 0:
                q.append(key)

        # pop from the queue and go to it's all neigbors to decrease their depedency number from 'in_degree' array
        while q:
            course = q.popleft()
            result.append(course)

            for neighbor in adjacency_list[course]:
                in_degree[neighbor] -= 1
                # if no dencey of the neighbor then add to the queue
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        # check all node presents in the result array
        if len(result) < numCourses - 1:
            return []

        return result