/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/lru-cache/}
 * @description Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
 */

class Node {
    constructor(value) {
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

        // put the node at first position

        // return the value
        return this.track_node[key].value;
    }

    /**
     * @param {number} key 
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        const new_node = new Node(value)

        this.track_node[key] = new_node
        this.move_to_first(new_node)

        // remove from tail
        console.log(this.length);
        if (this.capacity < this.length) {
            // console.log(this.capacity);
            // console.log(this.length);
            // console.log(this.tail);
            // console.log(this.tail.previous);
            this.tail = this.tail.previous
        }
    }

    move_to_first(new_node) {
        this.length++

        if (!this.cache) {
            this.cache = this.tail = new_node
            return
        }

        new_node.next = this.cache
        this.cache.previous = new_node
        this.cache = new_node
    }
}

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

const test = new LRUCache(2)
test.put(1, 3)
// console.log(test.cache);
test.put(2, 2)
// console.log(test.cache);
test.put(3, 1)
console.log(test.cache);