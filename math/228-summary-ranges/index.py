class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        res = []
        start, summaryRange = nums[0], str(nums[0])

        for i in range(1, len(nums)):
            if nums[i] == (start + 1):
                start += 1
                continue

            if start != int(summaryRange):
                summaryRange += '->' + str(start)
            res.append(summaryRange)
            start = nums[i]
            summaryRange = str(nums[i])

        if start != int(summaryRange):
            summaryRange += '->' + str(start)
        res.append(summaryRange)
        return res
