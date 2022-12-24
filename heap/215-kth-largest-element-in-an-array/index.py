class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = len(nums) - k

        def quickSelect(l, r):
            pivot, s = nums[r], l  # right most element as pivot

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[s], nums[i] = nums[i], nums[s]
                    s += 1
            nums[r], nums[s] = nums[s], nums[r]

            if kth > s:
                # go to right
                return quickSelect(s + 1, r)
            elif kth < s:
                # go to left
                return quickSelect(l, s - 1)
            else:
                # this is kth position
                return nums[s]

        return quickSelect(0, len(nums) - 1)