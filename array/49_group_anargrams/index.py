class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anargrams_map = {}

        for word in strs:
            char_count = [0] * 26

            for char in word:
                char_count[ord(char) - 97] +=  1

            anargram_key = '#'.join(map(str , char_count))

            if anargram_key in anargrams_map:
                anargrams_map[anargram_key].append(word)
            else:
                anargrams_map[anargram_key] = [word]

        return anargrams_map.values()