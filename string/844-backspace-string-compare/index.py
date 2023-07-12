# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution1:

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.removeSpace(s) == self.removeSpace(t)

    def removeSpace(self, s: str):
        stack = []

        for c in s:
            if c != '#':
                stack.append(c)
            elif len(stack):
                stack.pop()

        return ''.join(stack)


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution2:

    def backspaceCompare(self, S, T):
        i = len(S) - 1
        j = len(T) - 1

        skipS = 0
        skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i = i - 1

                elif skipS > 0:
                    skipS -= 1
                    i = i - 1

                else:
                    break

            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j = j - 1

                elif skipT > 0:
                    skipT -= 1
                    j = j - 1

                else:
                    break

            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False

            if (i >= 0) != (j >= 0):
                return False

            i = i - 1
            j = j - 1

        return True
