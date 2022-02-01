class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adjacency_list = [[] for _ in range(n)]

        for a , b in edges:
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