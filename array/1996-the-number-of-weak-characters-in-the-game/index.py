from typing import List


class Solution:

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        total = 0
        currMaxDefense = 0
        properties.sort(key=lambda x: (-x[0], x[1]))

        for _, d in properties:
            if d < currMaxDefense:
                total += 1
            else:
                currMaxDefense = d

        return total
