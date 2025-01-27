import collections
from typing import List


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj = collections.defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)

        prereqMap = {}
        res = []

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj[crs]:
                    prereqMap[crs] |= dfs(prereq)
                prereqMap[crs].add(crs)

            return prereqMap[crs]

        for crs in range(numCourses):
            dfs(crs)

        for u, v in queries:
            res.append(u in prereqMap[v])
        return res
