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
        const found_node = this.track_node[key]

        // if not present in cache return -1
        if (found_node === undefined) return -1

        // found at first position and has nothing to update
        if (!found_node.previous) return found_node.value

        // if found at last position or middle,then remove it
        if (key === this.tail.key) {
            this.remove_from_tail()
        } else {
            this.remove_from_middle(found_node)
        }

        // put the found node at first position
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
        const found_node = this.track_node[key]

        // if cache already has this key,then we need to update!
        if (found_node) {
            // found at first position, update its value
            if (!found_node.previous) {
                found_node.value = value
                return
            }

            // if found at last position or middle,then remove it
            if (key === this.tail.key) {
                this.remove_from_tail()
            } else {
                this.remove_from_middle(found_node)
            }

            this.length--
        }

        // if cache capacity exceeds
        if (this.capacity <= this.length) {
            // remove from tail
            const removed = this.remove_from_tail()
            // remove from the object
            delete this.track_node[removed.key]
            this.length--
        }

        // create new node
        const new_node = new Node(key, value)
        // put the new node at first position
        this.move_to_first(new_node)
        // keep record of the new node in key-value pair
        this.track_node[key] = new_node
        this.length++
    }

    /**
     * @description prepend a node at first position of the list
     * @param {*} new_node 
     * @returns 
     */
    move_to_first(new_node) {
        // if cache is empty then new_node will be pointed as head and tail both
        if (!this.length) {
            this.cache = this.tail = new_node
            return
        }

        // otherwise,prepend at head
        new_node.next = this.cache
        this.cache.previous = new_node
        this.cache = new_node
    }

    /**
     * @description remove a node from last position of the list 
     * @returns 
     */
    remove_from_tail() {
        const removedTail = this.tail;
        this.tail = this.tail.previous // update tail pointer
        removedTail.previous = null // close the connection

        if (this.tail) {
            this.tail.next = null // end of list
        } else {
            this.cache = null // list has no node after remove!
        }

        return removedTail
    }

    /**
     * @description remove node from middle of the list
     * @param {*} node 
     */
    remove_from_middle(node) {
        node.previous.next = node.next
        node.next.previous = node.previous
    }
}