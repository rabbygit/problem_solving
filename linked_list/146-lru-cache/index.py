class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = {}
        self.left, self.right = Node(0, 0), Node(0, 0)

        # left = LRU and right = most recent node
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.prev = prev
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            # remove and insert to right most position
            self.remove(self.nodeMap[key])
            self.insert(self.nodeMap[key])
            return self.nodeMap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            self.remove(self.nodeMap[key])

        # insert as right most
        self.nodeMap[key] = Node(key, value)
        self.insert(self.nodeMap[key])

        # check if capacity exceedes
        if len(self.nodeMap) > self.capacity:
            # remove left most node
            node = self.left.next
            self.remove(node)
            del self.nodeMap[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)