from typing import List


class Solution:

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def dfs(sub_result, sum, i):
            if sum == target:
                result.append(sub_result.copy())
                return

            if i >= n or sum > target:
                return

            sub_result.append(candidates[i])
            dfs(sub_result, sum + candidates[i], i)
            sub_result.pop()
            dfs(sub_result, sum, i + 1)

        dfs([], 0, 0)

        return result