/**
 * [Problem ref]{@link  https://leetcode.com/problems/word-search-ii/}
 * @description Given an m x n board of characters and a list of strings words,
 * return all words on the board.
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

  findWords(board) {
    const total_row = board.length
    const total_column = board[0].length
    const result = []
    const result_map = {}

    function backtrack(row, column, sub_result, current_root, visited) {
      const letter = board[row][column]
      if (!current_root || !current_root.letter_map[letter] || visited[`${row}${column}`]) {
        return
      }

      visited[`${row}${column}`] = true // track the position as visited
      current_root = current_root.letter_map[letter]

      // If it is the end of a word
      if (current_root.isWord && !result_map[sub_result + letter]) {
        result_map[sub_result + letter] = true // take only unique solution
        result.push(sub_result + letter)
      }

      // maximum 4 possible path can be possible for a position and we need to go every possible path
      if (column < total_column - 1) backtrack(row, column + 1, sub_result + letter, current_root, visited)
      if (column > 0) backtrack(row, column - 1, sub_result + letter, current_root, visited)
      if (row < total_row - 1) backtrack(row + 1, column, sub_result + letter, current_root, visited)
      if (row > 0) backtrack(row - 1, column, sub_result + letter, current_root, visited)

      visited[`${row}${column}`] = false
    }


    // go through every single position and try all possiblity
    for (let i = 0; i < total_row; i++) {
      for (let j = 0; j < total_column; j++) {
        backtrack(i, j, '', this.root, {})
      }
    }

    return result
  }
}

/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
const findWords = function (board, words) {
  // Add the words to trie
  const trie = new Trie()
  words.forEach(word => {
    trie.addWord(word)
  })

  return trie.findWords(board)
};