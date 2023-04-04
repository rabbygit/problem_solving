class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = ["JFK"]
        tickets.sort() # sort the tickets for lexical order
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
