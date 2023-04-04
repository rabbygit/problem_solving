import collections


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r < rows and r >= 0 and c < cols and c >= 0 and grid[r][
                            c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    total += 1

        return total