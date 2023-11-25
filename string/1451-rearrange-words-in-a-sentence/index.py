import collections


class Solution:

    def arrangeWords(self, text: str) -> str:
        result = ''
        textLength = len(text)
        textLenMap = collections.defaultdict(list)

        text = text.split(' ')
        text[0] = text[0].lower()

        for word in text:
            textLenMap[len(word)].append(word)

        for i in range(textLength):
            for w in textLenMap[i]:
                if len(result) == 0:
                    result += w.title()
                else:
                    result += ' ' + w

        return result
