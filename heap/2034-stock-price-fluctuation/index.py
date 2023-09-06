from heapq import heappush, heappop


class StockPrice:

    def __init__(self):
        self.priceMap = {}
        self.minHeap = []
        self.maxHeap = []
        self.latestTimestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        self.priceMap[timestamp] = price
        self.latestTimestamp = max(self.latestTimestamp, timestamp)

        # update min and max heap
        heappush(self.maxHeap, (-price, timestamp))
        heappush(self.minHeap, (price, timestamp))

    def current(self) -> int:
        return self.priceMap[self.latestTimestamp]

    def maximum(self) -> int:
        current, timestamp = heappop(self.maxHeap)

        while current * -1 != self.priceMap[timestamp]:
            current, timestamp = heappop(self.maxHeap)

        heappush(self.maxHeap, (current, timestamp))
        return current * -1

    def minimum(self) -> int:
        current, timestamp = heappop(self.minHeap)

        while current != self.priceMap[timestamp]:
            current, timestamp = heappop(self.minHeap)

        heappush(self.minHeap, (current, timestamp))
        return current
