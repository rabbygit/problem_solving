class MyCalendarTwo:
    # T.C: O(n^2) and S.C: O(n)
    def __init__(self):
        self.overlapping = []
        self.non_overlapping = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if not (start >= e or s >= end):
                return False

        for s, e in self.non_overlapping:
            if not (start >= e or s >= end):
                self.overlapping.append((max(s, start), min(e, end)))

        self.non_overlapping.append((start, end))
        return True
