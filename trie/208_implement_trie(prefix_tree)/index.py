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
        current_node = self.root

        for letter in word:
            if letter not in current_node.letter_map:
                return False
            else:
                current_node = current_node.letter_map[letter]

        if current_node.isWord:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root

        for letter in prefix:
            if letter not in current_node.letter_map:
                return False
            else:
                current_node = current_node.letter_map[letter]

        return True
