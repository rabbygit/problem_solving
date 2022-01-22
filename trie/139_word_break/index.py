class Node:
    def __init__(self, letter):
        self.letter = letter
        self.isWord = False
        self.letter_map = {}


class Trie:

    def __init__(self):
        self.root = Node('#')

    def insert(self, word: str) -> None:
        current_node = self.root

        for letter in word:
            if letter not in current_node.letter_map:
                current_node.letter_map[letter] = Node(letter)

            current_node = current_node.letter_map[letter]

        current_node.isWord = True

    def search(self, word: str) -> bool:
        n = len(word)
        u_set = set()

        def backtrack(i):
            if i in u_set:
                return False
            u_set.add(i)

            current_node = self.root

            for index in range(i,n):
                letter = word[index]
                if letter not in current_node.letter_map:
                    return False

                # move to child
                current_node = current_node.letter_map[letter]
                if current_node.isWord:   
                    if index == n-1:
                        return True                 
                    if backtrack(index + 1):
                        return True

            return False
        
        return backtrack(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()

        for word in wordDict:
            trie.insert(word)

        return trie.search(s)