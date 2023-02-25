import collections


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def bfs(r, c):
            q = collections.deque()
            area = 1
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r < rows and r >= 0 and c < cols and c >= 0 and grid[r][
                            c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1

            return area

        # visit every position
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    if area > maxArea:
                        maxArea = area

        return maxArea
