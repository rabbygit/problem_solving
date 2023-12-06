import collections
from typing import List


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        timeMap = collections.defaultdict(list)
        result = []

        for name, time in zip(keyName, keyTime):
            h, m = time.split(':')
            timeMap[name].append(int(h) * 60 + int(m))

        for name, time_list in timeMap.items():
            time_list.sort()

            for i in range(2, len(time_list)):
                curr = time_list[i]
                first = time_list[i - 2]
                if curr - first <= 60:
                    result.append(name)
                    break

        return sorted(result)