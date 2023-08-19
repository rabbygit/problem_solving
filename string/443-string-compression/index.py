class Solution:

    def compress(self, chars: List[str]) -> int:
        insertIdx, runnerIdx = 0, 0

        while runnerIdx < len(chars):

            chars[insertIdx] = chars[runnerIdx]
            count = 1

            while runnerIdx + 1 < len(chars) and chars[runnerIdx] == chars[
                    runnerIdx + 1]:
                runnerIdx += 1
                count += 1

            if count > 1:
                for c in str(count):
                    chars[insertIdx + 1] = c
                    insertIdx += 1

            runnerIdx += 1
            insertIdx += 1

        return insertIdx