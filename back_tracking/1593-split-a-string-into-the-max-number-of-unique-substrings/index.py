class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        uniqueSet = set()

        def dfs(i: int):
            if i == len(s):
                return 0

            res = 0
            for j in range(i, len(s)):
                sub_str = s[i : j + 1]
                if sub_str in uniqueSet:
                    continue
                uniqueSet.add(sub_str)
                res = max(res, 1 + dfs(j + 1))
                uniqueSet.remove(sub_str)

            return res

        return dfs(0)
