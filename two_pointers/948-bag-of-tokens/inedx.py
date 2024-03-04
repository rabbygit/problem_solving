from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = score = 0
        l, r = 0, len(tokens) - 1
        tokens.sort()

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                res = max(res, score)
                l += 1
            elif score:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break

        return res
