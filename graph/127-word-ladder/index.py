import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbor = collections.defaultdict(list)
        wordList.append(beginWord)
        q = collections.deque()
        visited = set()
        res = 1

        # build the adjaceny list for similar word pattern
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbor[pattern].append(word)

        q.append(beginWord)

        # run bfs to find the shortest path to endWord
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    
                    for node in neighbor[pattern]:
                        if node not in visited:
                            visited.add(node)
                            q.append(node)

            res += 1

        return 0

        
