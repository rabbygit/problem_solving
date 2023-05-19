class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        result = []
        lastOccur = {}
        partitionEnd = 0
        partitionSize = 0

        for idx, char in enumerate(s):
            lastOccur[char] = idx

        for idx, char in enumerate(s):
            partitionSize += 1
            partitionEnd = max(partitionEnd, lastOccur[char])

            if partitionEnd == idx:
                result.append(partitionSize)
                partitionSize = 0

        return result