class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        s_char = [0] * 26
        t_char = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_char[ord(s[i]) - 97] += 1
            t_char[ord(t[i]) - 97] += 1

        return '#'.join(map(str, s_char)) == '#'.join(map(str, t_char))