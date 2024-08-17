from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        prev_row = points[0]

        for r in range(1, rows):
            curr_row = points[r].copy()
            left_max, right_max = [0] * cols, [0] * cols
            left_max[0] = prev_row[0]
            right_max[cols - 1] = prev_row[cols - 1]

            for c in range(1, cols):
                left_max[c] = max(left_max[c - 1] - 1, prev_row[c])

            curr_row[cols - 1] += max(left_max[cols - 1], right_max[cols - 1])
            for c in range(cols - 2, -1, -1):
                right_max[c] = max(right_max[c + 1] - 1, prev_row[c])
                curr_row[c] += max(left_max[c], right_max[c])

            prev_row = curr_row

        return max(prev_row)
