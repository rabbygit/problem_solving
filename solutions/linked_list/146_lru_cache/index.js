/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/lru-cache/}
 * @description Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
 */

class Node {
    constructor(prev = null, val, next = null) {
        this.prev = prev
        this.val = val
        this.next = next
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
        const new_node = new Node(null, value, null)

        this.track_node[key] = new_node
        this.move_to_first(new_node)

        // remove from tail
        if (this.capacity >= this.length) {
            this.tail = this.tail.prev
        }
    }

    move_to_first(new_node) {
        if (this.cache) {
            this.cache.prev = new_node
        }
        new_node.next = this.cache
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
test.put(1, 1)
console.log(test.cache);
test.put(2, 2)
console.log(test.cache);
test.put(3, 3)
console.log(test.cache);