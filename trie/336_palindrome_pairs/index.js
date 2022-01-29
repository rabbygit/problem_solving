/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/palindrome-pairs/}
 * @description Given a list of unique words, 
 * return all the pairs of the distinct indices (i, j) in the given list, 
 * so that the concatenation of the two words words[i] + words[j] is a palindrome.
 */


class Node {
    constructor() {
        this.index = -1;
        this.letter_map = {};
        this.palindrom_list = []; // palindromes after this node
    }
}

class Trie {
    constructor() {
        this.root = new Node()
    }

    addWord(word, index) {
        let root = this.root;

        // add the word in trie in reverse order
        for (let i = word.length - 1; i >= 0; i--) {
            if (!root.letter_map[word[i]]){
                root.letter_map[word[i]] = new Node(); // initialize
            }

            // check upto is palindrome upto this letter from the beginning of the word
            if (isPalin(word, 0, i)){
                root.palindrom_list.push(index);
            }

            // move to child
            root = root.letter_map[word[i]];
        }

        // keep track of the word's index of words array
        root.index = index;
    }

    searchPalin(word) {
        let sub_result = [];
        let root = this.root;

        for (let index = 0; index < word.length; index++) {
            if (root.index >= 0 && isPalin(word,0,word.length-1)) {
                sub_result.push(root.index)
            }

            root = root.letter_map[word[index]]
            
            if (!root) {
                return sub_result
            }
        }

        // target is reversed base
        if (root.index >= 0) sub_result.push(root.index);

        // case 2
        sub_result.push(...root.palindrom_list);
        return sub_result;
    }
}

function isPalin(word, i, j) {
    while (i < j) if (word[i++] != word[j--]) return false;
    return true;
}

/**
 * @param {string[]} words
 * @return {number[][]}
 */
var palindromePairs = function (words) {
    let trie = new Trie();
    let result = [];
    for (let i = 0; i < words.length; i++) {
        trie.addWord(words[i], i);
    }

    for (let i = 0; i < words.length; i++) {
        let candidates = trie.searchPalin(words[i]);
        for (let c of candidates) {
            if (i === c) {
                continue
            }

            result.push([i, c]);
        }
    }

    return result;
}