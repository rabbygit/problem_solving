from typing import List


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # [{temparatur, index}]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temperature, index = stack.pop()
                result[index] = i - index

            stack.append([t, i])

        return result
