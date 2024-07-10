from typing import List


class Solution:
    # T.C: O(n) and S.C: O(1)
    def minOperations(self, logs: List[str]) -> int:
        steps = 0

        for log in logs:
            if log == "../":
                steps -= 1
                # reset to 0 for negative value
                steps = max(steps, 0)
            elif log != "./":
                steps += 1

        return steps
