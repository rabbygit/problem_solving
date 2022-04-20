/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/valid-anagram/}
 * @description Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
 * typically using all the original letters exactly once.
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = function(s, t) {
    const s_len = s.length
    const t_len = t.length
    const s_map = {}
    const t_map = {}

    if(s_len !== t_len) return false;

    for (let index = 0; index < s_len; index++) {
        if (s_map[s[index]] === undefined) {
            s_map[s[index]] = 1
        }else{
            s_map[s[index]]++
        }

        if (t_map[t[index]] === undefined) {
            t_map[t[index]] = 1
        }else{
            t_map[t[index]]++
        }
    }

    for (const [key, value] of Object.entries(s_map)) {
        if (t_map[key] === undefined || t_map[key] !== value) {
            return false
        }
    }

    return true
};