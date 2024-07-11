class Solution:

    def reverseParentheses(self, s):
        opened = []
        pair = {}

        for i, c in enumerate(s):
            if c == "(":
                opened.append(i)
            if c == ")":
                j = opened.pop()
                pair[i], pair[j] = j, i

        res = []
        i, d = 0, 1

        while i < len(s):
            if s[i] in "()":
                i = pair[i]
                d = -d
            else:
                res.append(s[i])

            i += d
        return "".join(res)


class Solution1:
    # T.C: O(n * m), m is the number of pairs and S.C: O(n)
    def reverseParentheses(self, s):
        stack = []

        for c in s:
            if c == ")":
                reversed_word = []
                while stack[-1] != "(":
                    reversed_word.append(stack.pop())
                
                stack.pop() # remove the "("
                
                # append the reversed characters again to the stack
                for rc in reversed_word:
                    stack.append(rc)
            else:
                stack.append(c)

        return "".join(stack)
