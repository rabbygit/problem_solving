class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        res = ''
        stack = []

        for c in s:
            if not stack or stack[-1]['char'] != c:
                stack.append({'char': c, 'count': 1})
            else:
                stack[-1]['count'] += 1
                if stack[-1]['count'] == k:
                    stack.pop()

        for e in stack:
            res += e['char'] * e['count']

        return res
