from typing import List


class Solution:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line, length = [], 0
        i = 0

        while i < len(words):
            # line is complete
            if length + len(line) + len(words[i]) > maxWidth:
                total_spaces = maxWidth - length
                even_spaces = total_spaces // max(1, len(line) - 1)
                reminder = total_spaces % max(1, len(line) - 1)

                # distribute spaces
                for j in range(max(1, len(line) - 1)):
                    line[j] += ' ' * even_spaces
                    if reminder:
                        line[j] += ' '
                        reminder -= 1

                result.append("".join(line))
                line, length = [], 0 # reset

            line.append(words[i])
            length += len(words[i])
            i += 1

        # handle last line
        last_line = " ".join(line)
        trailing_spaces = maxWidth - len(last_line)
        result.append(last_line + ' ' * trailing_spaces)

        return result