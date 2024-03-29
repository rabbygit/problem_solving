import collections


class Solution:
    """ Kahn's algorithm for Topological Sorting
        1. remove node which has zero indegree
        2. decrease indegree value for all the dependend nodes of that removed node
        3. Repeat
    """

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:

        adjacency_list = collections.defaultdict(list)
        indegree = {}
        q = collections.deque()

        # create adjacency_list, calculate indegree
        for src, des in prerequisites:
            adjacency_list[des].append(src)
            indegree[des] = indegree.get(des, 0)
            indegree[src] = indegree.get(src, 0) + 1

        # add all the nodes to queue that have zero indegree to process
        for key in range(numCourses):
            if key not in indegree or indegree[key] == 0:
                q.append(key)

        count = 0
        while q:
            course = q.popleft()
            count += 1

            # decrease indegree value for all the dependend course
            for dependend_course in adjacency_list[course]:
                indegree[dependend_course] -= 1

                # if the course has no indegree then add to the queue
                if indegree[dependend_course] == 0:
                    q.append(dependend_course)

        return count == len(adjacency_list)

    def canFinish1(self, numCourses: int,
                   prerequisites: List[List[int]]) -> bool:
        visited = set()
        adjacency_list = collections.defaultdict(list)

        # create adjacency_list
        for crs, pre in prerequisites:
            adjacency_list[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            if len(adjacency_list[crs]) == 0:
                return True

            visited.add(crs)
            for pre in adjacency_list[crs]:
                if not dfs(pre): return False

            visited.remove(crs)
            adjacency_list[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False

        return True