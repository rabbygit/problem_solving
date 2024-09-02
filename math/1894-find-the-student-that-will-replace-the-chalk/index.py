from typing import List


class Solution:
    # T.C: O(n) and S.C: O(1)
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # total chalks needed to completed one cycle
        totalChalkNeeded = sum(chalk)
        # remaining chalks after possible cycles completion
        reamins = k % totalChalkNeeded

        # find where the remaining chalks are not sufficient
        for idx, chalkNeeded in enumerate(chalk):
            if chalkNeeded > reamins:
                return idx

            reamins -= chalkNeeded
