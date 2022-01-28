class Node:
    def __init__(self, letter):
        self.letter = letter
        self.isWord = False
        self.letter_map = {}


class WordDictionary:

    def __init__(self):
        self.root = Node('#')

    def addWord(self, word: str) -> None:
        current_node = self.root

        for letter in word:
            if letter not in current_node.letter_map:
                current_node.letter_map[letter] = Node(letter)

            current_node = current_node.letter_map[letter]

        current_node.isWord = True

    def search(self, word: str) -> bool:

        def backtrack(j,root):
            current_node = root

            for index in range(j , len(word)):
                letter = word[index]
                if letter == '.':
                    for possible_root in current_node.letter_map.values():
                        if backtrack(index + 1 , possible_root):
                            return True
                    return False
                else:
                    if letter not in current_node.letter_map:
                        return False
                    current_node = current_node.letter_map[letter]
            
            return current_node.isWord

        return backtrack(0,self.root)
