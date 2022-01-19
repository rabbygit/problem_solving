class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index>self.length or index<0:
            return -1; # Invalid index
        if self.length == 0:
            return self.head # Empty linked list
        
        i = 0
        temp = self.head
        while i < self.length:
           val = temp.val
           temp = temp.next
           i+=1
           print("gfhgghff")
        return val
            
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        # create new node
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("1----> ",self.head.val)
        else:
            new_node.next = self.head
            self.head = new_node
            print("2----> ",self.head.val)
            
        self.length +=1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        

my_list = MyLinkedList()
print(my_list.addAtHead(5))
print(my_list.get(1))
print(my_list.addAtHead(6))
print(my_list.get(1))