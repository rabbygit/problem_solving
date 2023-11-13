import collections
from typing import List

class Solution:
    # time complexity: O(E) + E * log E
    # space complexity: O(E)
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        tickets.sort(reverse=True)
        res, stack = [], ["JFK"]

        for src, dst in tickets:
            graph[src].append(dst)

        while stack:
            c = stack[-1]
            if c in graph and len(graph[c]):
                stack.append(graph[c].pop())
            else:
                res.append(stack.pop())

        return list(reversed(res))

    # got TLE, time complexity: E * log E + E ^ d where d is the maximum number of outgoing flights from a particular airport.
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = ["JFK"]
        tickets.sort()  # sort the tickets for lexical order
        adj = {src: [] for src, dst in tickets}

        for src, dst in tickets:
            adj[src].append(dst)

        def dfs(src):
            # base case, we reach all the tickets
            if len(result) == len(tickets) + 1:
                return True

            # no destination for this source
            # we have to go back and try with another source
            if src not in adj:
                return False

            temp = list(adj[src])
            for idx, node in enumerate(temp):
                adj[src].pop(idx)
                result.append(node)

                if dfs(node):
                    return True

                adj[src].insert(idx, node)
                result.pop()

            return False

        dfs("JFK")

        return result
