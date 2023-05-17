class Solution:

    def mergeTriplets(self, triplets: List[List[int]],
                      target: List[int]) -> bool:
        mergeableIndex = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for idx, value in enumerate(t):
                if target[idx] == value:
                    mergeableIndex.add(idx)

        return len(mergeableIndex) == 3
