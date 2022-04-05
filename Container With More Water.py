class Solution:
    def maxArea(self, height: List[int]) -> int:
        mi, v, m = 0, 0, 0
        left = 0
        right = len(height) - 1
        while left < right :
            mi = min(height[left], height[right])
            v = mi * (right - left)
            m = max(m, v)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return m
