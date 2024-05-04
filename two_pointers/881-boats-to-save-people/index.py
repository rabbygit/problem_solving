from typing import List


class Solution:
    # T.C: O(nlogn) and S.C: O(n)
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        totalBoats = 0
        people.sort()

        while l <= r:
            # take the heavy person
            rem = limit - people[r]

            # check if we can take the light person too
            if l != r and rem >= people[l]:
                l += 1

            r -= 1
            totalBoats += 1

        return totalBoats
