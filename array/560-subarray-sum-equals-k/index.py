class Solution:
    # related problem: path sum iii. link: https://leetcode.com/problems/path-sum-iii/
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        prefix_map = {}
        result = 0

        for num in nums:
            current_sum += num

            if current_sum == k:
                result += 1

            result += prefix_map.get(current_sum - k, 0)

            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

        return result
