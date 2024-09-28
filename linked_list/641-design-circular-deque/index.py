class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.maxSize = k
        self.length = 0
        self.head = Node("#")
        self.tail = Node("#")
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        newHead = Node(value)
        currHead = self.head.next

        currHead.prev = newHead
        newHead.next = currHead

        newHead.prev = self.head
        self.head.next = newHead

        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        currTail = self.tail.prev
        newTail = Node(value)

        newTail.prev = currTail
        currTail.next = newTail

        newTail.next = self.tail
        self.tail.prev = newTail

        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        newHead = self.head.next.next
        self.head.next = newHead
        newHead.prev = self.head

        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        newTail = self.tail.prev.prev
        newTail.next = self.tail
        self.tail.prev = newTail

        self.length -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.value

    def isEmpty(self) -> bool:
        return not bool(self.length)

    def isFull(self) -> bool:
        return self.length == self.maxSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
