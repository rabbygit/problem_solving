class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        outgoingPath = set()

        for a, _ in paths:
            outgoingPath.add(a)

        for _, b in paths:
            if b not in outgoingPath:
                return b