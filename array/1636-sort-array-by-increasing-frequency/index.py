import collections


class Solution:

    def frequencySort(self, nums: List[int]) -> List[int]:
        numMap = collections.Counter(nums)
        return sorted(nums, key=lambda x: (numMap[x], -x))