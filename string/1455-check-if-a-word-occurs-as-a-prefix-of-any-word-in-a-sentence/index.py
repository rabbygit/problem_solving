class Solution:
    # T.C: O(n) and S.C: O(1)
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        i = idx = wordIdx = wordLen = 0
        k = len(searchWord)

        while i < len(sentence):
            if sentence[i] != " ":
                wordLen += 1
                if wordLen == 1:
                    wordIdx += 1
                    while (
                        i < len(sentence) and idx < k and searchWord[idx] == sentence[i]
                    ):
                        idx += 1
                        i += 1

                    if idx == k:
                        return wordIdx

            if i < len(sentence) and sentence[i] == " ":
                wordLen = 0
                idx = 0

            i += 1

        return -1
