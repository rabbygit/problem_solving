/**
 * [Problem ref]{@link  https://leetcode.com/problems/word-break/}
 * @description Given a string s and a dictionary of strings wordDict, 
 * return true if s can be segmented into a space-separated sequence of one or more dictionary words.
 */


class Node {
    constructor(letter) {
        this.letter = letter // letter like: a/b/c
        this.isWord = false // For marking if it is the last letter of the word
        this.letter_map = {} // map all related letter's address
    }
}

class Trie {
    constructor() {
        this.root = new Node('#')
    }

    /**
    * @param {string} word
    * @return {void}
    */
    insert(word) {
        let current_node = this.root

        // loop through every element and add to trie if already not add
        for (let index = 0; index < word.length; index++) {
            const letter = word[index]
            if (!current_node.letter_map[letter]) {
                current_node.letter_map[letter] = new Node(letter)
            }
            current_node = current_node.letter_map[letter]
        }

        current_node.isWord = true // mark the last element as the end of a word
    }

    /** 
    * @param {string} word
    * @return {boolean}
    */
    search(word) {
        let n = word.length
        let set = new Set() // to store unique index

        const backtrack = (i) => {
            // check from this index already visited
            // visited indicates loop
            if (set.has(i)) {
                return false
            }

            set.add(i) // add current index to track later

            let current_node = this.root

            // loop through every element and check letter's existence
            for (let index = i; index < n; index++) {
                const letter = word[index]
                if (!current_node.letter_map[letter]) {
                    return false
                }

                current_node = current_node.letter_map[letter] // move to child
                if (current_node.letter_map[letter].isWord) {
                    if (index === n - 1) {
                        return true
                    }

                    if (backtrack(index + 1)) {
                        return true
                    }
                }
            }

            return false
        }

        return backtrack(0) // start from the initial position
    };
}

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
const wordBreak = function (s, wordDict) {
    const trie = new Trie()
    // construct the trie
    wordDict.forEach(word => {
        trie.insert(word)
    });

    return trie.search(s)
};