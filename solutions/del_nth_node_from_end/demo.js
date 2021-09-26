class Node {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

/**
 * Initialize your data structure here.
 */
class MyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    addAtHead(val) {
        // create new node 
        let new_node = new Node(val, this.head);
        this.head = new_node;
    }

    delete() {
        // delete nth element
        console.log("head", this.head)
        let current_node = this.head;
        let previous;
        for (let i = 0; i < 2; i++) {
            previous = current_node;
            current_node = current_node.next; // next node
        }
        previous.next = previous.next.next

        console.log(this.head)
    }
};

const list = new MyLinkedList()
list.addAtHead(3)
list.addAtHead(2)
list.addAtHead(1)
list.delete()