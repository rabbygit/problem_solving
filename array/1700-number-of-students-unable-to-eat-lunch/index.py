import collections
from typing import List


class Solution:
    # T.C: O(n) and S.C: O(n)
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwichPref = collections.Counter(students)
        k = 0

        while k < len(sandwiches) and sandwichPref[sandwiches[k]] > 0:
            sandwichPref[sandwiches[k]] -= 1
            k += 1

        return len(sandwiches) - k