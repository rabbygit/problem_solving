from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for i in range(len(result)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or result[i] != strs[j][i]:
                    return result[:i]

        return result