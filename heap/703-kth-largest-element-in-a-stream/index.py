import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        while self.k < len(self.minHeap):
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]