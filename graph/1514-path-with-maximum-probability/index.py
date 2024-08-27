import heapq
import collections
from typing import List


class Solution:
    # T.C: O(E log V) or V^2, S.C: O(E+V)
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        # build the adjacency list
        adj = collections.defaultdict(list)
        for idx in range(len(edges)):
            s, e = edges[idx]
            adj[s].append([e, succProb[idx]])
            adj[e].append([s, succProb[idx]])

        maxHeap = [(-1, start_node)]
        visited = set()

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            visited.add(node)

            if node == end_node:
                return prob * -1

            # visit the neighbors and append in the maxHeap
            # so, when we will pop, it will be the maximum probability
            for nei, new_prob in adj[node]:
                if nei not in visited:
                    heapq.heappush(maxHeap, (prob * new_prob, nei))

        return 0
