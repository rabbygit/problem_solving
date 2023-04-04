import collections


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # count total fresh oranges and
        # keep rotten to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        while q and fresh > 0:

            # pop all rotten oranges
            for i in range(len(q)):
                r, c = q.popleft()

                # go to possible 4 directions and find fresh one
                # make fresh to rotten and add to
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if row >= 0 and col >= 0 and row < rows and col < cols and grid[
                            row][col] == 1:

                        q.append([row, col])
                        grid[row][col] = 2
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1
