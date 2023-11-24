class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh = totalMin = 0
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while q:
            length = len(q)
            rotten = False
            for _ in range(length):
                r, c = q.popleft()

                for dr, dc in dir:
                    row, col = r + dr, c + dc
                    if row > -1 and row < rows and col > -1 and col < cols and grid[
                            row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
                        rotten = True

            if rotten: totalMin += 1

        return totalMin if fresh == 0 else -1
