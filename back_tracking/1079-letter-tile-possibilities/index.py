import collections


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = collections.Counter(tiles)

        def backtrack():
            res = 0

            for c in count:
                if count[c] > 0:
                    res += 1
                    count[c] -= 1
                    res += backtrack()
                    count[c] += 1
            
            return res
        
        return backtrack()