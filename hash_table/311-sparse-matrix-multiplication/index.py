from collections import defaultdict
from typing import List


class Solution:
    # https://assets.leetcode.com/uploads/2021/03/12/mult-grid.jpg
    def multiply(self, mat1: List[List[int]],
                 mat2: List[List[int]]) -> List[List[int]]:
        # Interviewer expects us to store the matrix efficiency and do multiplication using that.
        # We will create some buckets where each bucket denotes one ’row‘ and that bucket
        # contains an array of pairs of (value, column).

        def compressMatrix(mat):
            dic = defaultdict(list)

            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if mat[i][j] != 0:
                        dic[i].append([mat[i][j], j])

            return dic

        dic1 = compressMatrix(mat1)
        dic2 = compressMatrix(mat2)
        result = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for mat1_row in dic1.keys():
            for ele1, mat1_col in dic1[mat1_row]:
                if mat1_col not in dic2:
                    continue
                for ele2, mat2_col in dic2[mat1_col]:
                    result[mat1_row][mat2_col] += ele1 * ele2

        return result