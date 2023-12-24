class Node:

    def __init__(self, data):
        self.next = None
        self.data = data


class MyQueue1:

    def __init__(self):
        self.head = Node('#')
        self.tail = self.head

    def push(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next

    def pop(self):
        val = self.head.next.data
        self.head.next.data = '#'
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.next.data

    def empty(self):
        return self.head.next is None


class MyQueue:

    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def move(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()