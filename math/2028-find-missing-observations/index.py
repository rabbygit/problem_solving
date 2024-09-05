from typing import List


class Solution:
    # T.C: O(n) and S.C: O(1)
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missingSum = (len(rolls) + n) * mean - sum(rolls)
        if missingSum > n * 6 or missingSum < n:
            return []

        res = []
        while n:
            possibleValue = min(6, missingSum - n + 1)
            missingSum -= possibleValue
            res.append(possibleValue)
            n -= 1

        return res
