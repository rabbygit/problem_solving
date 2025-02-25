from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = even = res = curr_sum = 0
        MOD = 10**9 + 7

        for n in arr:
            curr_sum += n

            if curr_sum % 2:
                res = (1 + res + even) % MOD
                odd += 1
            else:
                res = (res + odd) % MOD
                even += 1

        return res
