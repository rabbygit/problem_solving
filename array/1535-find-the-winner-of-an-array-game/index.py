class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        currMax = arr[0]
        winCount = 0

        for i in range(1, len(arr)):
            if arr[i] > currMax:
                currMax = arr[i]
                winCount = 0
            winCount += 1

            if winCount == k:
                return currMax

        return currMax