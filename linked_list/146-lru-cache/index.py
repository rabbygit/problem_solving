class Node:

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currSize = 0
        self.nodeMap = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node: Node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def addNodeToHead(self, node: Node):
        temp = self.head.next
        self.head.next = temp.prev = node
        node.prev = self.head
        node.next = temp

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]
        self.removeNode(node)
        self.addNodeToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.nodeMap:
            node = Node(key, value)
            self.addNodeToHead(node)
            self.nodeMap[key] = node
            self.currSize += 1
        else:
            self.removeNode(self.nodeMap[key])
            node = Node(key, value)
            self.addNodeToHead(node)
            self.nodeMap[key] = node

        if self.currSize > self.capacity:
            node = self.tail.prev
            self.removeNode(node)
            del self.nodeMap[node.key]
            self.currSize -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)