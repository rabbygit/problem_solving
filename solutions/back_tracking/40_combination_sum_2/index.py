from operator import le


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        # sort the elements to keep same element side by side like [1,2,3,1] to [1,1,2,3]
        candidates.sort()

        def generate_combination(sub_result, sum, i):
            if sum == target:
                temp = sub_result[:]
                result.append(temp)
                return

            if sum > target:
                return

            for index in range(i, n):
                # skip duplicate value and move to next element
                if i != index and candidates[index] == candidates[index-1]:
                    continue

                sub_result.append(candidates[index])
                generate_combination(
                    sub_result, sum+candidates[index], index+1)
                sub_result.pop()

        generate_combination([], 0, 0)

        return result
