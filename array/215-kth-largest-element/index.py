import heapq


class Solution:
    # T.C: O(n log k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for n in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, n)
            else:
                if n > minHeap[0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, n)

        return minHeap[0]
