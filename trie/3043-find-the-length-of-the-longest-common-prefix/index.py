from typing import List

# Time Complexity: O(m⋅log10 M + n⋅log 10 N)
# O(m⋅log 10 M)
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr2) > len(arr1):
            return self.longestCommonPrefix(arr2, arr1)

        prefix_set = set()
        res = 0
        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n = n // 10

        for n in arr2:
            while n and n not in prefix_set:
                n = n // 10

            if n:
                res = max(res, len(str(n)))

        return res


class TrieNode:
    def __init__(self) -> None:
        self.children = {}


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, num):
        curr_node = self.root
        num_str = str(num)

        for digit in num_str:
            if digit not in curr_node.children:
                curr_node.children[digit] = TrieNode()
            curr_node = curr_node.children[digit]

    def find_longest_prefix(self, num):
        curr_node = self.root
        num_str = str(num)
        prefix_length = 0

        for digit in num_str:
            if digit not in curr_node.children:
                break

            prefix_length += 1
            curr_node = curr_node.children[digit]

        return prefix_length


class Solution2:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr2) > len(arr1):
            return self.longestCommonPrefix(arr2, arr1)

        res = 0
        trie = Trie()
        for n in arr1:
            trie.insert(n)

        for n in arr2:
            prefix_length = trie.find_longest_prefix(n)
            res = max(res, prefix_length)

        return res
