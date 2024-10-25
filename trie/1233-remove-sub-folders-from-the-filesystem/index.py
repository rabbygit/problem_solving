class Node:
    def __init__(self):
        self.isEnd = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, folder: str):
        folder = folder.split("/")
        curr = self.root

        for path in folder:
            if path not in curr.children:
                curr.children[path] = Node()
            curr = curr.children[path]
        curr.isEnd = True

    def isSubFolder(self, folder: str) -> bool:
        folder = folder.split("/")
        curr = self.root
        result = False

        for idx, path in enumerate(folder):
            next_node = curr.children[path]
            if next_node.isEnd and idx != len(folder) - 1:
                result = True
                break
            curr = next_node

        return result


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result = []
        trie = Trie()

        for path in folder:
            trie.insert(path)

        for path in folder:
            if not trie.isSubFolder(path):
                result.append(path)

        return result
