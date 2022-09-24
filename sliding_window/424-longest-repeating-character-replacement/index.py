class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0
        maxCount = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = 1 + count.get(char, 0)
            maxCount = max(maxCount, count[char])

            if right - left + 1 - maxCount > k:
                count[s[left]] -= 1
                left += 1

            result = max(result , right - left + 1)

        
        return result