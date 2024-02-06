from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            tmp = arr[i]
            arr[i] = currMax
            currMax = max(currMax, tmp)

        return arr