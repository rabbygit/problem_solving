/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/lru-cache/}
 * @description Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
 */

class Node {
    constructor(key, value) {
        this.key = key
        this.value = value
        this.previous = null
        this.next = null
    }
}

class LRUCache {
    /**
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = capacity
        this.length = 0
        this.track_node = {}
        this.cache = null
        this.tail = null
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        // if not present in cache return -1
        if (this.track_node[key] === undefined) {
            return -1;
        }

        const found_node = this.track_node[key]
        const previous_node = found_node.previous

        // found at first position
        if (!previous_node) {
            return found_node.value;
        }

        console.log(this.tail);
        // found at last position
        if (found_node.key === this.tail.key) {
            this.remove_from_tail()
        } else {
            previous_node.next = found_node.next
            found_node.previous = previous_node
        }

        // put the node at first position
        const new_node = new Node(key, found_node.value)
        this.move_to_first(new_node)
        this.track_node[key] = new_node

        // return the value
        return found_node.value;
    }

    /**
     * @param {number} key 
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        if (this.track_node[key] !== undefined) {
            const found_node = this.track_node[key]
            const previous_node = found_node.previous

            // found at first position
            if (!previous_node) {
                found_node.value = value
                return
            }

            // found at last position
            if (found_node.key === this.tail.key) {
                // this.tail = this.tail.previous
                // this.tail.next = null
                this.remove_from_tail()
            } else {
                previous_node.next = found_node.next
                found_node.previous = previous_node
            }

            this.length--
        }

        // if cache capacity exceeds
        if (this.capacity <= this.length) {
            // remove from tail
            this.length--
            const removed = this.remove_from_tail()

            // remove from the object
            delete this.track_node[removed.key]
        }

        // create new node
        const new_node = new Node(key, value)
        // put the new node at first position
        this.move_to_first(new_node)
        // keep record of the new node in key-value pair
        this.track_node[key] = new_node
        this.length++
    }

    move_to_first(new_node) {
        if (!this.cache) {
            this.cache = this.tail = new_node
            return
        }

        new_node.next = this.cache
        this.cache.previous = new_node
        this.cache = new_node
    }

    remove_from_tail() {
        const removedTail = this.tail;
        this.tail = this.tail.previous

        if (this.tail) {
            this.tail.next = null
        } else {
            this.cache = null
        }

        return removedTail
    }
}

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

const test = new LRUCache(3)
test.put(1, 1)
test.put(2, 2)
test.put(3, 3)
test.put(4, 4)


console.log(test.get(4));
console.log(test.get(3));
// console.log(test.get(2));
// // console.log(test.get(1));

// test.put(5, 5)

// console.log(test.get(1));
// console.log(test.get(2));
// console.log(test.get(3));
// console.log(test.get(4));
// console.log(test.get(5));


// console.log(test.tail);

// console.log('HEADDDDDDDDDDDDDDD');

console.log(test.cache);