# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:

    def firstBadVersion(self, n: int) -> int:
        l, r, mid = 1, n, 1

        while l <= r:
            mid = l + (r - l) // 2
            if isBadVersion(mid) and isBadVersion(mid - 1) == False:
                return mid
            elif isBadVersion(mid) and isBadVersion(mid - 1):
                r = mid - 1
            else:
                l = mid + 1

        return mid