from typing import List


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # [[temparature, index], ...n]

        for idx, tem in enumerate(temperatures):
            while stack and stack[-1][0] < tem:
                _, stackIdx = stack.pop()
                result[stackIdx] = idx - stackIdx
            stack.append([tem, idx])

        return result
