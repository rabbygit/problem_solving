class Solution:

    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0

        while target > 1:
            if not maxDoubles:
                steps += (target - 1)
                break
            elif target % 2 == 0 and maxDoubles:
                target = target / 2
                steps += 1
                maxDoubles -= 1
            else:
                target -= 1
                steps += 1

        return steps