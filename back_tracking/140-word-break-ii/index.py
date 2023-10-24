class Solution:
    # ref: https://www.youtube.com/watch?v=8DV-cXg6Rh0
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}

        def dfs(string: str):
            if string in cache:
                return cache[string]

            if not string:
                return ['']

            res = []
            for w in wordDict:
                if string.startswith(w):
                    for word in dfs(string[len(w):]):
                        res.append(w + (' ' if word else '') + word)

            cache[string] = res
            return cache[string]

        return dfs(s)