class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                genrate_combination(sub_result, sum + candidate, index+1)
                sub_result.pop()

                # skip next duplicate value
                while index + 1 < n and candidates[index] == candidates[index+1]:
                    index += 1
                
                index += 1

        genrate_combination([], 0, 0)

        return result