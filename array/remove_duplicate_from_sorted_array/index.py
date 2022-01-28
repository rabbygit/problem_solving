
# Problem ref: 26. https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 0  # for keep tracking of last unique element
        length = len(nums)

        while i < length:
            # assign new element
            k += 1
            nums[k-1] = nums[i]

            # loop through to find same elements
            for j in range(i+1, length):
                if(nums[j] != nums[i]):
                    break
                else:
                    # same element and pass
                    i += 1

            # increment the counter
            i += 1

        return k

    # Imroved soltuion
    # Runtime: 0(n)
    def removeDuplicates2(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0

        j = 1
        k = 1
        replace_idx = 1

        for i in range(length-1):
            if nums[i] != nums[j]:
                nums[replace_idx] = nums[j]
                replace_idx += 1
                k += 1

            j += 1

        return k
