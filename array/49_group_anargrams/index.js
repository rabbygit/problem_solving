/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/group-anagrams/}
 * @description Given an array of strings strs, group the anagrams together. 
 * You can return the answer in any order.
 */


/**
 * @description Runtime O(n * k)
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagrams = function (strs) {
    const anargram_map = {}

    strs.forEach(word => {
        const char_count = new Array(26).fill(0)

        // count character occurence of a word
        for (let index = 0; index < word.length; index++) {
            char_count[word.charCodeAt(index) - 97]++
        }

        // and make the occurence array as a key and check
        const anargram_key = char_count.join()
        if (anargram_map[anargram_key] === undefined) {
            anargram_map[anargram_key] = [word]
        } else {
            anargram_map[anargram_key].push(word)
        }
    });

    return Object.values(anargram_map)
};