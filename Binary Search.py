class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        while l<= h:
            m = l + ((h - l) >> 1)
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                h = m - 1
        return -1
