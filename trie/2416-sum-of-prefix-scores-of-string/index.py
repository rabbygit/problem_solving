import collections
from typing import List


class Solution:
    # T.C and S.C: O(n * l^2)
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        result = [0] * len(words)
        prefix_count = collections.defaultdict(int)

        for idx, w in enumerate(words):
            for i in range(len(w)):
                prefix = w[: i + 1]
                prefix_count[prefix] += 1

        for idx, w in enumerate(words):
            count = 0
            for i in range(len(w)):
                prefix = w[: i + 1]
                count += prefix_count[prefix]
            result[idx] = count

        return result


# Solution with trie
class TrieNode:
    def __init__(self, count) -> None:
        self.count = count
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode(0)

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode(0)
            curr.children[ch].count += 1
            curr = curr.children[ch]

    def sum_of_prefix(self, word: str) -> int:
        curr = self.root
        count = 0

        for ch in word:
            if ch not in curr.children:
                break
            count += curr.children[ch].count
            curr = curr.children[ch]

        return count
    
class Solution:
    # T.C and S.C: O(n * l)
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        result = []

        trie = Trie()
        for word in words:
            trie.insert(word)
        
        for word in words:
            result.append(trie.sum_of_prefix(word))

        return result