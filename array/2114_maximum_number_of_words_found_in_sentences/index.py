class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0

        for sentence in sentences:
            length = len(sentence.split())
            if length > count:
                count = length
        
        return count