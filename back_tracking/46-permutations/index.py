class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        taken = set()
        n = len(nums)

        def genratePermute(sub_result):
            if len(sub_result) == n:
                result.append(sub_result.copy())
                return

            for num in nums:
                if num not in taken:
                    taken.add(num)
                    sub_result.append(num)
                    genratePermute(sub_result)
                    sub_result.pop()
                    taken.remove(num)

        genratePermute([])

        return result