class Solution:

    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        # equal string but have duplicate char, then it's possible to swap
        # ex: s=aa and goal=aa(possible), s=ab and goal=ab(not possible)
        if s == goal and len(set(s)) < len(s):
            return True

        # find how many characters are different
        # we are allowed to swap only two characters
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        if len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[
                diff[1]] == goal[diff[0]]:
            return True

        return False