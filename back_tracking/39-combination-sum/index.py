class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def genrate_combination(sub_result, sum, i):
            if sum == target:
                result.append(sub_result.copy())
                return

            if sum > target:
                return

            for index in range(i, n):
                candidate = candidates[index]
                sub_result.append(candidate)
                genrate_combination(sub_result, sum + candidate, i)
                sub_result.pop()
                i += 1

        genrate_combination([], 0, 0)

        return result