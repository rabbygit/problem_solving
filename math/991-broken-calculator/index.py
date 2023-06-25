class Solution:

    # https://leetcode.com/problems/broken-calculator/solutions/234484/java-c-python-change-y-to-x-in-1-line/comments/310757/
    def brokenCalc(self, startValue: int, target: int) -> int:
        steps = 0

        while target > startValue:
            steps += 1
            if target % 2 == 0:
                target /= 2
            else:
                target += 1

        steps += startValue - target
        return steps