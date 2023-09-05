import collections


class SnapshotArray:

    def __init__(self, length: int):
        self.snapVersions = collections.defaultdict(dict)
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        obj = self.snapVersions[self.snapId]
        obj[index] = val

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id, -1, -1):
            obj = self.snapVersions[i]
            if index in obj:
                return obj[index]

        return 0


# improved version with binary search
class SnapshotArray(object):

    def __init__(self, n):
        self.A = [[[0, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        currSnapId = self.A[index][-1][0]
        if currSnapId == self.snap_id:
            self.A[index][-1][1] = val
        else:
            self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        arr = self.A[index]
        left, right, ans = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        if ans == -1: return 0
        return arr[ans][1]
