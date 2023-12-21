import collections
from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n, result = len(nums), []
        count_map = collections.Counter(nums)
        count_array = [[] for i in range(n + 1)]

        # build array for occurence from hashMap. like [ [] , [] , [] , [], [1,2 ..] ]
        for key, value in count_map.items():
            count_array[value].append(key)

        # build the result
        for i in range(n, 0, -1):
            for num in count_array[i]:
                result.append(num)
                # check k element is taken already or not
                if len(result) == k:
                    return result