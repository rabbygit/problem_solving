from typing import List


class TrieNode:
    def __init__(self):
        self.count = 0
        self.childs = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.childs:
                curr.childs[ch] = TrieNode()

            curr = curr.childs[ch]
            curr.count += 1


    def isSubString(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            curr = curr.childs[ch]
        return curr.count > 1
        
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        trie = Trie()

        for word in words:
            for startIdx in range(len(word)):
                trie.insert(word[startIdx:])

        for word in words:
            if trie.isSubString(word):
                res.append(word)
        
        return res