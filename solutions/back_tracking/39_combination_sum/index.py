class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        i = 0

        def genrate_combination(sub_result,sum,i):
            if sum == target:
                temp = sub_result[:]
                result.append(temp)
                return

            if sum > target:
                return

            for index in range(i,n):
                candidate = candidates[index]
                sum += candidate
                sub_result.append(candidate)
                genrate_combination(sub_result,sum,i)
                sum -= candidate
                sub_result.pop()
                i+=1


        genrate_combination([],0,i)

        return result