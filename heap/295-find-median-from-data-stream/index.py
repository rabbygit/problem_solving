import heapq


class MedianFinder:

    def __init__(self):
        # split the data stream into two heap
        self.maxHeap = []
        self.minHeap = []
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1 * num)

        # check if maxHeap has larger num than minHeap
        if (self.maxHeap and self.minHeap
                and -1 * self.maxHeap[0] > self.minHeap[0]):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1 * val)

        # distribute nums evenly
        if (len(self.maxHeap) > len(self.minHeap) + 1):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        if (len(self.minHeap) > len(self.maxHeap) + 1):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * val)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        elif len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]
        else:
            return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()