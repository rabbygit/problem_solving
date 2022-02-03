from typing import List
from collections import deque


class Solution:
    # DFS approach
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        destination = len(graph) - 1  # destination node
        result = []

        def dfs(node: int, sub_result: List[int]):
            sub_result.append(node)  # append the node

            # check if this node is the destination
            if node == destination:
                result.append(sub_result.copy())
                return

            # get all adjacent nodes of the node
            next_nodes = graph[node]

            # call recursively for each adjacent node
            for index in range(len(next_nodes)):
                dfs(next_nodes[index], sub_result)
                sub_result.pop()

        dfs(0, [])
        return result

    # BFS approach
    def BFS(self, graph: List[List[int]]) -> List[List[int]]:
        destination = len(graph) - 1  # destination node
        result = []

        queue = deque()
        queue.append([0])

        while queue:
            sub_path = queue.popleft()
            node = sub_path[-1]  # last node of the path

            for neighbor in graph[node]:
                # concate neighbor with current sub_path
                temp = sub_path.copy()
                temp.append(neighbor)

                if neighbor == destination:
                    result.append(temp)
                else:
                    # concated path
                    queue.append(temp)

        return result
