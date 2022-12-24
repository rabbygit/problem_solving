import heapq


class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        # making weight negative to make a maxHeap
        stones = [-weight for weight in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                # subtract from smaller(actually, it's the bigger)
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])