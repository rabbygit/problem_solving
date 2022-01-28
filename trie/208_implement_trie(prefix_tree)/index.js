/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/implement-trie-prefix-tree/}
 * @description A trie (pronounced as "try") or prefix tree is a tree data structure
 * used to efficiently store and retrieve keys in a dataset of strings.
 * There are various applications of this data structure, such as autocomplete and spellchecker.
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
    let current_node = this.root

    // loop through every element and check letter's existence
    for (let index = 0; index < word.length; index++) {
      const letter = word[index]
      if (!current_node.letter_map[letter]) {
        return false
      } else {
        current_node = current_node.letter_map[letter]
      }
    }

    // check wheteher it is a word or not
    if (current_node.isWord) return true

    // otherwise return false
    return false
  };

  /** 
  * @param {string} prefix
  * @return {boolean}
  */
  startsWith(prefix) {
    let current_node = this.root

    // loop through every element and check letter's existence
    for (let index = 0; index < prefix.length; index++) {
      const letter = prefix[index]
      if (!current_node.letter_map[letter]) {
        return false
      } else {
        current_node = current_node.letter_map[letter]
      }
    }

    return true
  };
}