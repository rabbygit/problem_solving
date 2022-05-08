class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_exists = set(nums)
        longest_sequence = 0

        for num in nums:
            if not num-1 in nums_exists:
                current_num = num
                sequence_length = 1

                while current_num+1 in nums_exists:
                    current_num += 1
                    sequence_length += 1

                longest_sequence = max(longest_sequence,sequence_length)

        
        return longest_sequence