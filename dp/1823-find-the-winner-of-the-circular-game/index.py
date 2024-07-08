import collections


class Solution:
    # T.C and S.C: O(n)
    def findTheWinner(self, n: int, k: int) -> int:
        q = collections.deque()

        for i in range(1, n + 1):
            q.append(i)

        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())
            q.popleft()

        return q[0]


class Solution1:
    # T.C: O(n) and S.C: O(1)
    # explanation: https://www.youtube.com/watch?v=PBBQgW_75e0
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0

        for i in range(1, n + 1):
            res = (res + k) % i

        return res + 1
