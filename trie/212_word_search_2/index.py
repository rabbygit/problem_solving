
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

    def findWords(self, board):
        total_row = len(board)
        total_column = len(board[0])
        result = []
        result_map = set()

        def backtrack(row, column, sub_result, current_root, visited):
            letter = board[row][column]
            if not current_root or letter not in current_root.letter_map or (row, column) in visited:
                return

            visited.add((row, column))  # track the position as visited
            current_root = current_root.letter_map[letter]

            # If it is the end of a word
            if current_root.isWord and (sub_result+letter) not in result_map:
                result_map.add(sub_result+letter)  # take only unique solution
                result.append(sub_result+letter)

            #  maximum 4 possible path can be possible for a position and we need to go every possible path
            if (column < total_column - 1):
                backtrack(row, column + 1, sub_result +
                          letter, current_root, visited)
            if (column > 0):
                backtrack(row, column - 1, sub_result +
                          letter, current_root, visited)
            if (row < total_row - 1):
                backtrack(row + 1, column, sub_result +
                          letter, current_root, visited)
            if (row > 0):
                backtrack(row - 1, column, sub_result +
                          letter, current_root, visited)

            visited.remove((row, column))

        # go through every single position and try all possiblities
        for i in range(total_row):
            for j in range(total_column):
                backtrack(i, j, '', self.root, set())

        return result


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        # add all word to trie
        for word in words:
            trie.insert(word)

        return trie.findWords(board)
