class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.idx = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value

        res = []
        while self.idx < len(self.stream) and self.stream[self.idx]:
            res.append(self.stream[self.idx])
            self.idx += 1

        return res