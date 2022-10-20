/**
 * [Problem ref]{@link  https://leetcode.com/problems/palindrome-pairs/}
 * @description Given a list of unique words, 
 * return all the pairs of the distinct indices (i, j) in the given list, 
 * so that the concatenation of the two words words[i] + words[j] is a palindrome.
 */

class Trie {
    constructor() {
        this.children = {};
        this.word = null;
        this.index = null;
    }
}

/**
 * @param {string[]} words
 * @return {number[][]}
 */
const palindromePairs = function (words) {
    const root = new Trie();
    const res = []

    for (let i = 0; i < words.length; i++) {
        if (!words[i]) continue;
        buildTrie(root, words[i], i)
    }

    for (let i = 0; i < words.length; i++) {
        const isEmptyChar = !words[i];
        searchPrefix(words[i], root, res, i, isEmptyChar)
    }

    return res;
};

function buildTrie(root, word, index) {
    let node = root;

    // build the trie in reverse order
    for (let i = word.length - 1; i >= 0; i--) {
        const c = word[i];
        if (!node.children[c]) node.children[c] = new Trie();
        node = node.children[c]
    }

    node.word = word;
    node.index = index;
}

function searchPrefix(prefix, root, res, initialIndex, isEmptyChar) {
    let node = root;

    for (let i = 0; i < prefix.length; i++) {
        const w = prefix[i];
        if (!node.children[w]) {
            return res;
        }

        if (node.children[w].word && i < prefix.length - 1) {
            // if the child node is already a word, 
            // and we want to check if remainder of the prefix builds is a palindrome, 
            // then we have a match
            checkIfMatch(node.children[w], res, prefix.substring(i + 1), initialIndex, isEmptyChar)
        }

        node = node.children[w];
    }

    // here we search for the past the entire prefix
    dfs(node, res, '', initialIndex, isEmptyChar)
    return res;
}

function dfs(node, res, str, initialIndex, isEmptyChar) {
    checkIfMatch(node, res, str, initialIndex, isEmptyChar)
    for (let c in node.children) {
        const s = str + c;
        dfs(node.children[c], res, s, initialIndex, isEmptyChar)
    }
}

function checkIfMatch(node, res, str, initialIndex, isEmptyChar) {
    if (node.word && isPalindrome(str) && node.index !== initialIndex) {
        pushIntoResults(initialIndex, node.index, res)
        if (isEmptyChar) {
            pushIntoResults(node.index, initialIndex, res)
        }
    }
}

function pushIntoResults(index1, index2, res) {
    res.push([index1, index2])
}

function isPalindrome(s) {
    let end = s.length - 1;
    for (let start = 0; start < s.length / 2; start++) {
        if (s[start] !== s[end]) return false;
        end--;
    }
    return true;
}