class Node:

    def __init__(self):
        self.isWord = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]

        curr.isWord = True

    def findWords(self, board):
        rows, cols = len(board), len(board[0])
        result = set()

        def backtrack(r, c, sub_result, node):
            letter = board[r][c]
            if not node or letter not in node.children or board[r][c] == '#':
                return

            # track the position as visited
            tmp = board[r][c]
            board[r][c] = '#'
            node = node.children[letter]

            # it's the end of a word and take only unique solution
            if node and node.isWord:
                result.add(sub_result + letter)

            # maximum 4 possible path can be possible for a position
            # and we need to go every possible path
            if (c < cols - 1):
                backtrack(r, c + 1, sub_result + letter, node)
            if (c > 0):
                backtrack(r, c - 1, sub_result + letter, node)
            if (r < rows - 1):
                backtrack(r + 1, c, sub_result + letter, node)
            if (r > 0):
                backtrack(r - 1, c, sub_result + letter, node)

            board[r][c] = tmp

        # go through every single position and try all possiblities
        for i in range(rows):
            for j in range(cols):
                backtrack(i, j, '', self.root)

        return list(result)


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        # add all words to the trie data structure
        for word in words:
            trie.insert(word)

        return trie.findWords(board)
