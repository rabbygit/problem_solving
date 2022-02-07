import collections
import heapq
from typing import List
 
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create the adjacency list of nodes/vertex
        adjacency_list = collections.defaultdict(list)
        for s , d , w in times:
            adjacency_list[s].append((d,w))

        heap = [(0,k)] # keep starting node and it's weight
        visited = set() # to track visited node

        while heap:
            time , node = heapq.heappop(heap) # pop the minimum available weighted node
            
            # check if it's already visited or not
            if node in visited:
                continue
            
            # add the node to visited set
            visited.add(node)
            
            # when all nodes are visited that means signal completes traversing to all nodes
            # since this is the last visited node,all nodes receive the signal by this time
            # so return the time it takes to reach this node
            if len(visited) == n:
                return time
            
            # add all adjacent nodes of the node which are not visited yet
            for neighbor , ne_time in adjacency_list[node]:
                if neighbor not in visited:
                    # add the time it takes to come this node
                    heapq.heappush(heap , (ne_time+time,neighbor))

        return -1