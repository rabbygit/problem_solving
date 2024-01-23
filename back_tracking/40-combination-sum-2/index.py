from typing import List


class Solution:

    def combinationSum2WithoutLoop(self, candidates: List[int],
                                   target: int) -> List[List[int]]:

        n, res = len(candidates), []
        candidates.sort()

        def backtrack(i: int, subSum: int, subRes: List[int]):
            if subSum == target:
                res.append(subRes.copy())
                return

            if i >= n or subSum > target:
                return

            subRes.append(candidates[i])
            backtrack(i + 1, subSum + candidates[i], subRes)

            subRes.pop()
            while i + 1 < n and candidates[i + 1] == candidates[i]:
                i += 1

            backtrack(i + 1, subSum, subRes)

        backtrack(0, 0, [])
        return res

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()

        def genrate_combination(sub_result, sum, i):
            if sum == target:
                result.append(sub_result.copy())
                return

            if sum > target:
                return

            index = i
            while index < n:
                candidate = candidates[index]
                sub_result.append(candidate)
                genrate_combination(sub_result, sum + candidate, index + 1)
                sub_result.pop()

                # skip next duplicate value
                while index + 1 < n and candidates[index] == candidates[index +
                                                                        1]:
                    index += 1

                index += 1

        genrate_combination([], 0, 0)

        return result