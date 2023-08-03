class Solution:

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        result = [[0 for j in range(m)] for i in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]

        return result