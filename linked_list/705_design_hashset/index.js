/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/design-hashset/}
 * @description Design a HashSet without using any built-in hash table libraries.
 */


class MyHashSet {
    constructor() {
        this.hashSet = new Array(769).fill(false)
    }

    hash(key) {
        // reduce collision by using prime numbers
        return key % 769
    }

    /** 
     * @param {number} key
     * @return {void}
     */
    add(key) {
        // calculate hash key
        // check if it's already used or not
        // if used then add the node to linked list
        const calculated_hash = this.hash(key)
        if (this.hashSet[calculated_hash]) {
            let node = this.hashSet[calculated_hash]

            while (node.next) {
                if (node.val === key) return;
                node = node.next
            }

            if (node.val === key) return;

            node.next = {
                val: key,
                next: null
            }
        } else {
            this.hashSet[calculated_hash] = {
                val: key,
                next: null
            }
        }
    };

    /** 
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        const calculated_hash = this.hash(key)
        let node = this.hashSet[calculated_hash]
        let prev = null

        while (node) {
            if(node.val === key){
                if(prev){
                    prev.next = node.next
                }else{
                    this.hashSet[calculated_hash] = node.next
                }

                break;
            }
            prev = node
            node = node.next
        }
    };

    /** 
     * @param {number} key
     * @return {boolean}
     */
    contains(key) {
        const calculated_hash = this.hash(key)
        let node = this.hashSet[calculated_hash]
        while(node){
            // key found
            if (node.val === key) return true;
            node = node.next
        }

        return false
    };
};