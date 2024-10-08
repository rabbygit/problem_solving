class Solution:
    def minSwaps(self, s: str) -> int:
        close = maxClose = 0

        for brac in s:
            if brac == "]":
                close += 1
                maxClose = max(maxClose, close)
            else:
                close -= 1

        return (maxClose + 1) // 2
