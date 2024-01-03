from typing import List


class Solution:

    def numberOfBeams(self, bank: List[str]) -> int:
        prev = result = 0

        for row in bank:
            curr = 0
            for cell in row:
                if cell == '1':
                    curr += 1

            result += prev * curr
            
            if curr > 0:
                prev = curr

        return result