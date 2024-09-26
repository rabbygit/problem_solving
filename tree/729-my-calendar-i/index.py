class MyCalendar:
    # T.C: O(n^2) and S.C: O(n)
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.events:
            if not (start >= e or end <= s):
                return False
        self.events.append([start, end])
        return True


class Tree:
    # T.C: O(n logn) and S.C: O(n)
    def __init__(self, start: int, end: int) -> None:
        self.left = None
        self.right = None
        self.start = start
        self.end = end

    def insert(self, start: int, end: int) -> bool:
        curr = self
        while True:
            if start >= curr.end:
                if not curr.right:
                    curr.right = Tree(start, end)
                    return True
                curr = curr.right
            elif end <= curr.start:
                if not curr.left:
                    curr.left = Tree(start, end)
                    return True
                curr = curr.left
            else:
                return False

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Tree(start, end)
            return True
        return self.root.insert(start, end)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
