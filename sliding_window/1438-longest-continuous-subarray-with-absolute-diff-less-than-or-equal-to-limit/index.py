import collections


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_length = 1
        n = len(nums)
        # We defined the two monotonic array here
        increasing_q = collections.deque()
        decreasing_q = collections.deque()

        # Start sliding -_- ...
        for right in range(n):
            # remember we should always try to insert the value into the last of the monotonic arrays
            # For increasing_q, check whether the last value of the monotonic array is larger than the right end of the window.
            # If it is,then need to pop the value until we find the one which is smaller than the right end of the window
            # insert the right end of the window at the last of the increasing monotonic array.
            # You cannot put the increasing_q[-1] >= nums[right] here because the limit might be 0 and in this case,
            # we need to count the number of equal value.
            while increasing_q and increasing_q[-1] > nums[right]:
                increasing_q.pop()
            increasing_q.append(nums[right])

            # For decreasing_q, check whether the last value of the monotonic array is smaller than the right end of the window.
            # If it is, then need to pop the value until we find the one which is larger than the right end of the window
            # and insert the right end of the window at the last of the decreasing monotonic array.
            # You cannot put the decreasing_q[-1] <= nums[right] here because the limit might be 0 and in this case,
            # we need to count the number of equal value.
            while decreasing_q and decreasing_q[-1] < nums[right]:
                decreasing_q.pop()
            decreasing_q.append(nums[right])

            # we need to check if the difference of the max and min in the current window is bigger than the limit or not,
            # if it is, we need to do something and update our window.
            while decreasing_q[0] - increasing_q[0] > limit:
                # For decreasing_q, there are 3(actually I think there are only 2) cases here:
                # nums[left] is greater than decreasing_q[0], then it must have been popped before
                # nums[left] == decreasing_q[0], then pop it here
                # nums[left] is smaller than decreasing_q[0](which I think is impossible because we should always pop the bigger ones first to get the smaller ones
                # so we haven't reached those nums which are smaller than decreasing_q[0] yet.)
                if decreasing_q[0] == nums[left]:
                    decreasing_q.popleft()
                # For increasing_q, there are 3(actually I think there are only 2) cases here:
                # nums[left] is smaller than increasing_q[0], then it must have been popped before
                # nums[left] == increasing_q[0], then pop it here
                # nums[left] is greater than increasing_q[0](which I think is impossible because we should always pop the smaller ones first to get the bigger ones so we haven't reached those nums which are bigger than increasing_q[0] yet.)
                if increasing_q[0] == nums[left]:
                    increasing_q.popleft()

                # We need to update the left here to forward our window so that it is more likely to be valid
                left += 1
            # window is valid 😊, update the max_length here.
            max_length = max(max_length, right - left + 1)
        return max_length
