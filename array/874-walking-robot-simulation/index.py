from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # [N, E, S, W]
        obstaclesSet = {tuple(o) for o in obstacles}
        x = y = res = dir = 0

        for c in commands:
            if c == -1:
                # move right
                dir = (dir + 1) % 4
            elif c == -2:
                # move left
                dir = (dir - 1) % 4
            else:
                dx, dy = directions[dir]
                for _ in range(c):
                    # check if obstacle is in this co-ordinate
                    if (x + dx, y + dy) in obstaclesSet:
                        break
                    # forward one step at a time
                    x, y = x + dx, y + dy

                res = max(res, x**2 + y**2)

        return res
