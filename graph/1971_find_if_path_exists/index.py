from typing import List
from collections import deque


class Solution:
    # DFS approach
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adjacency_list = [[] for _ in range(n)]

        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        stack = [start]
        seen = set()

        while stack:
            # pop the last inserted node
            node = stack.pop()

            # check if the node is our target node
            if node == end:
                return True

            # check if the node is already visited or not
            if node in seen:
                continue
            seen.add(node)

            # add all neighbor nodes of the node to stack
            for neighbor in adjacency_list[node]:
                stack.append(neighbor)

        return False

    # BFS approach
    def BFS(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adjacency_list = [[] for _ in range(n)]

        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        queue = deque([start])
        seen = set(start)

        while queue:
            # pop the first inserted node
            node = queue.popleft()

            # check if the node is our target node
            if node == end:
                return True

            # add all neighbor nodes of the node to stack
            for neighbor in adjacency_list[node]:
                if not neighbor in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return False
