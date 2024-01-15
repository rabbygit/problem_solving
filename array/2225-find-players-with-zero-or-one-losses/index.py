from typing import List


class Solution:

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = [[], []]
        lossCount = [None] * 100001

        for w, l in matches:
            if lossCount[w] == None:
                lossCount[w] = 0
            else:
                lossCount[w] += 0

            if lossCount[l] == None:
                lossCount[l] = 1
            else:
                lossCount[l] += 1

        for player in range(100001):
            if lossCount[player] == 0:
                res[0].append(player)
            elif lossCount[player] == 1:
                res[1].append(player)

        return res
