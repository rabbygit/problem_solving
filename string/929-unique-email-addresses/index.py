from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            local, domain = e.split('@')
            local = local.split('+')[0].replace('.', '')
            unique.add(local+'@'+domain)

        return len(unique)