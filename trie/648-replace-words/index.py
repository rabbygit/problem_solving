class Node:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]

        node.isWord = True

    def search(self, word) -> str:
        node = self.root
        root = ""

        for c in word:
            if c not in node.children:
                return word

            root += c
            node = node.children[c]
            if node.isWord:
                return root

        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        result = []

        for word in dictionary:
            trie.insert(word)

        for word in sentence.split():
            result.append(trie.search(word))

        return " ".join(result)
