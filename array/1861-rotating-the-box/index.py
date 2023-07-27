from typing import List


class Solution:

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        r, c = len(box), len(box[0])
        result = [["" for x in range(r)] for y in range(c)]

        for i in range(r):
            empty = c - 1
            for j in range(c - 1, -1, -1):
                cell = box[i][j]
                if cell == "*":
                    empty = j - 1
                elif cell == "#":
                    box[i][j] = "."
                    box[i][empty] = "#"
                    empty -= 1

        for i in range(r):
            for j in range(c - 1, -1, -1):
                result[j][r - i - 1] = box[i][j]

        return result