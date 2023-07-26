import math
from typing import List


class Solution:

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        total_group = math.ceil(len(s) / k)

        for i in range(1, total_group):
            sub_str = s[(i - 1) * k:i * k]
            if len(sub_str) < k:
                sub_str += fill * (k - len(sub_str))
            result.append(sub_str)

        return result
