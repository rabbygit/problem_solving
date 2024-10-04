import collections
from typing import List


class Solution:
    # T.C: O(n logn) and S.C: O(n)
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        teamSkill = skill[0] + skill[-1]

        for i in range(0, len(skill) // 2 + 1):
            if skill[i] + skill[len(skill) - 1 - i] != teamSkill:
                return -1
            chemistry += skill[i] * skill[len(skill) - 1 - i]

        return chemistry


class Solution1:
    # T.C: O(n) and S.C: O(n)
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        target = total // (len(skill) // 2)

        if total % target:
            return -1

        count = collections.Counter(skill)
        chemistry = 0

        for s in skill:
            if not count[s]:
                continue

            diff = target - s
            if not count[diff]:
                return -1

            chemistry += s * diff
            count[s] -= 1
            count[diff] -= 1

        return chemistry
