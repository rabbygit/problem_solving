import heapq
from collections import deque, Counter


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        occurence = Counter(tasks)
        maxHeap = [-count for count in occurence.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)  # decrease count
                if count:
                    queue.append([
                        count, time + n
                    ])  # keep count and available time to add to heap

            # pop from queue and add to heap if idle time is over
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time
