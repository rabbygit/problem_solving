from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        deq = deque() # indices in decreasing manner
        left , right = 0

        while right < len(nums):
            # pop out all smaller values than current right value 
            while deq and nums[deq[-1]] < nums[right]:
                deq.pop()
            
            # append the right index
            deq.append(right)

            # pop the left most index from queue when left index of window passed that index
            if left > deq[0]:
                deq.popleft()

            # take the max of window from queue
            if (right + 1) >= k:
                result.append(nums[deq[0]])
                left += 1

            right += 1

        return result 