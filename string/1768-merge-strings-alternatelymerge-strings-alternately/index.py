class Solution:
    # Time & Space Complexity: O(n)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        len1, len2 = len(word1), len(word2)
        res = []

        while i < len1 and j < len2:
            res.append(word1[i])
            res.append(word1[j])
            i += 1
            j += 1

        if i < len1:
            res.append(word1[i:])
        elif j < len2:
            res.append(word2[j:])

        return "".join(res)
