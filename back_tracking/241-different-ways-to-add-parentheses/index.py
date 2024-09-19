from typing import List


class Solution:
    # T.C: O(n * 2^n) and S.C: O(2^n)
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }

    def diffWaysToCompute(self, expression: str) -> List[int]:
        def backtrack(l, r):
            res = []

            for i in range(l, r + 1):
                op = expression[i]
                if op in self.operations:
                    # compute left possible expression part
                    left_res = backtrack(l, i - 1)
                    # compute right possible expression part
                    right_res = backtrack(i + 1, r)

                    # compute the whole expression
                    for n1 in left_res:
                        for n2 in right_res:
                            res.append(self.operations[op](n1, n2))

            if res == []:
                res = [int(expression[l : r + 1])]

            return res

        return backtrack(0, len(expression) - 1)
