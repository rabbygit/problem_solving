"""
A string can be abbreviated by replacing any number of non-adjacent, 
non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

1. "s10n" ("s ubstitutio n")
2. "sub4u4" ("sub stit u tion")
3. "12" ("substitution")
4. "su3i1u2on" ("su bst i t u ti on")
5. "substitution" (no substrings replaced)

The following are not valid abbreviations:

1. "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
2. "s010n" (has leading zeros)
3. "s0ubstitution" (replaces an empty substring)

Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
A substring is a contiguous non-empty sequence of characters within a string.
"""


class Solution:

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # word = "internationalization", abbr = "i12iz4n"
        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False

                k = j
                while k < len(abbr) and abbr[k].isdigit():
                    k += 1
                num = int(abbr[j:k])
                i += num
                j = k
            else:
                return False

        return i == len(word) and j == len(abbr)