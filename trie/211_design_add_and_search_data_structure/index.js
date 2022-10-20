/**
 * [Problem ref]{@link  https://leetcode.com/problems/design-add-and-search-words-data-structure/}
 * @description Design a data structure that supports adding new words and 
 * finding if a string matches any previously added string.
 */

class Node {
    constructor(letter) {
        this.letter = letter // letter like: a/b/c
        this.isWord = false // For marking if it is the last letter of the word
        this.letter_map = {} // map all related letter's address
    }
}

class WordDictionary {
    constructor() {
        this.root = new Node('#')
    }

    /**
    * @param {string} word
    * @return {void}
    */
    addWord(word) {
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
        function backtrck(j, root) {
            let current_node = root

            // loop through every element and check letter's existence
            for (let index = j; index < word.length; index++) {
                const letter = word[index]
                if (letter === '.') {
                    for (const [, possible_root] of Object.entries(current_node.letter_map)) {
                        if (backtrck(index + 1, possible_root)) {
                            return true
                        }
                    }
                    return false
                } else {
                    if (!current_node.letter_map[letter]) return false
                    current_node = current_node.letter_map[letter]
                }
            }

            // wheteher it is a word or not
            return current_node.isWord
        }

        backtrck(0, this.root)
    };
}