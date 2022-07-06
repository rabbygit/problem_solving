class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] < height[right]:
                largest_area = max(largest_area , height[left] * (right - left))
                left += 1
            else:
                largest_area = max(largest_area , height[right] * (right - left))
                right -= 1

        return largest_area
