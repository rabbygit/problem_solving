class LinkedList:

    def __init__(self, pair) -> None:
        self.pair = pair
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hash = [None] * self.size

    def hashKey(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self.hashKey(key)

        if not self.hash[idx]:
            self.hash[idx] = LinkedList((key, value))
        else:
            prev = curr = self.hash[idx]

            while curr:
                if curr.pair[0] == key:
                    curr.pair = (key, value)
                    return
                prev = curr
                curr = curr.next

            prev.next = LinkedList((key, value))

    def get(self, key: int) -> int:
        idx = self.hashKey(key)
        curr = self.hash[idx]

        while curr:
            if curr.pair[0] == key:
                return curr.pair[1]
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        idx = self.hashKey(key)
        prev = curr = self.hash[idx]

        if not curr: return
        if curr.pair[0] == key:
            self.hash[idx] = curr.next

        while curr:
            if curr.pair[0] == key:
                next = curr.next
                prev.next = next
                break

            prev = curr
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# simple solution
class MyHashMap1:

    def __init__(self):
        self.map = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key] if self.map[key] is not None else -1

    def remove(self, key: int) -> None:
        self.map[key] = None