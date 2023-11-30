from typing import List


class Compare(str):

    def __lt__(x, y):
        return x + y < y + x


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        nums.sort(key=Compare, reverse=True)
        return '0' if nums[0] == '0' else "".join(nums)
