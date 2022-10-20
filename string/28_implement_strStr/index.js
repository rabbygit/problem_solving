/**
 * [Problem ref]{@link  https://leetcode.com/problems/implement-strstr/}
 * @description Given two strings needle and haystack, 
 * return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 */

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
const strStr = function (haystack, needle) {
    const map = {}
    const needle_len = needle.length

    if (!needle_len) return 0;

    for (let index = 0; index < haystack.length; index++) {
        const str_part = haystack.slice(index, needle_len + index)
        if (str_part.length === needle_len && map[str_part] === undefined) {
            map[str_part] = index
        }
    }

    return map[needle] !== undefined ? map[needle] : -1;
};