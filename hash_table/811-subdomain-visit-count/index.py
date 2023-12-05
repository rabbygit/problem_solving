import collections
from typing import List


class Solution:

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        countMap = collections.defaultdict(int)
        result = []

        for d in cpdomains:
            count, domain = d.split(' ')
            count = int(count)

            countMap[domain] += count
            if len(domain.split('.')) > 2:
                sub1, sub2 = domain.split('.')[-2:]
                countMap[sub2] += count
                countMap[sub1 + '.' + sub2] += count
            else:
                sub2 = domain.split('.')[-1]
                countMap[sub2] += count

        for k, v in countMap.items():
            result.append(str(v) + " " + k)

        return result