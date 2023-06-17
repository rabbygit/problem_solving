class Solution:

    def sortString(self, s: str) -> str:
        freq = [0] * 26
        res = ''

        # make an array to keep the frequency of every char
        for i in range(len(s)):
            freq[ord(s[i]) - 97] += 1

        while len(res) < len(s):
            # add the char to the result in increasing order
            for i in range(len(freq)):
                if freq[i]:
                    res += chr(i + 97)
                    freq[i] -= 1

            # add the char to the result in decreasing order
            for i in range(len(freq) - 1, -1, -1):
                if freq[i]:
                    res += chr(i + 97)
                    freq[i] -= 1

        return res