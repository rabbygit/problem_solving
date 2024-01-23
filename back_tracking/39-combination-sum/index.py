from typing import List


class Solution:

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        n, res = len(candidates), []

        def backtrack(i: int, subSum: int, subRes: List[int]):
            if subSum == target:
                res.append(subRes.copy())
                return

            if i >= n or subSum > target:
                return

            subRes.append(candidates[i])
            backtrack(i, subSum + candidates[i], subRes)

            subRes.pop()
            backtrack(i + 1, subSum, subRes)

        backtrack(0, 0, [])
        return res