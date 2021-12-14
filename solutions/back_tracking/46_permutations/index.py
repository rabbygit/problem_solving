class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.taken = {}
        self.n = len(nums)

        def genratePermute(sub_result):
            if len(sub_result) == self.n:
                r = sub_result[:]
                self.result.append(r)

            for i in range(self.n):
                if not nums[i] in self.taken or not self.taken[nums[i]]:
                    self.taken[nums[i]] = True
                    sub_result.append(nums[i])
                    genratePermute(sub_result)
                    sub_result.pop()
                    self.taken[nums[i]] = False

        genratePermute([])

        return self.result