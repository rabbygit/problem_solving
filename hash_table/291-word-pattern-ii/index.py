class Solution:
    """
    ref1: https://leetcode.com/problems/word-pattern-ii/solutions/73664/share-my-java-backtracking-solution/
    ref2: https://leetcode.com/problems/word-pattern-ii/solutions/3855540/python-backtracking-with-great-variables-names-easy-for-understanding/

    Time complexity: the problem is more like slicing the string into m pieces.
    How many slicing ways? C(n^m).
    For each slice, it takes O(n) to validate.
    So the total complexity is O(n * C(n^m))
    """
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        charToWord = {}
        wordToChar = {}

        def backtrack(pIdx, sIdx):
            # reached to end of the pattern
            if pIdx == len(pattern):
                return sIdx == len(s)

            p = pattern[pIdx]
            if p in charToWord:
                word = charToWord[p]
                if s[sIdx:sIdx + len(word)] != word:
                    return False

                # word matched, continue searching
                return backtrack(pIdx + 1, sIdx + len(word))
            else:
                for k in range(1, len(s) - sIdx + 1):
                    word = s[sIdx:sIdx + k]
                    if word in wordToChar:
                        continue

                    charToWord[p] = word
                    wordToChar[word] = p
                    if backtrack(pIdx + 1, sIdx + len(word)):
                        return True

                    # try with different char set
                    del charToWord[p]
                    del wordToChar[word]

        return backtrack(0, 0)
