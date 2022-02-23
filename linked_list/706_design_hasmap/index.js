/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/design-hashmap/}
 * @description Design a HashMap without using any built-in hash table libraries.
*/

// This problem can also be solved by using hash function and linked list to avoid collisions
// which is similar to 705. design hashset problem
// but this time it's done using only big array
class MyHashMap {
    constructor(){
        // to accomulate 10^6 keys
        this.map = new Array(1000001)
    }

    /** 
     * @param {number} key 
     * @param {number} value
     * @return {void}
    */
    put(key, value) {
        this.map[key] = value
    };

    /** 
     * @param {number} key
     * @return {number}
     */
    get(key) {
        return this.map[key] !== undefined ? this.map[key] : -1
    };

    /** 
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        delete this.map[key]
    };
};