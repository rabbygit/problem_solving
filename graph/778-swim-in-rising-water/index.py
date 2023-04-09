import heapq

class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]  # time, row, column
        visited.add((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            # bottom right position
            if r == n - 1 and c == n - 1:
                return t

            # go to 4 possible direction and add to minHeap
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc

                if neiR < 0 or neiR == n or neiC < 0 or neiC == n or (
                        neiR, neiC) in visited:
                    continue

                visited.add((neiR, neiC))
                heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])