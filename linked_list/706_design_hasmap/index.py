class MyHashMap:

    def __init__(self):
        self.map = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key] if self.map[key] is not None else -1

    def remove(self, key: int) -> None:
        self.map[key] = None