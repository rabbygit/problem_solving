class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)  # total length of list
        total_possibility = pow(2, n)  # possible number of subset

        def backtrack(sub_result, i):
            # all possible subset found
            if len(result) == total_possibility:
                return

            # append the sub solution
            temp = sub_result[:]
            result.append(temp)

            # loop through every element and find all possibles
            for index in range(i, n):
                sub_result.append(nums[index])
                backtrack(sub_result, index+1)
                sub_result.pop()

        backtrack([], 0)

        return result
