class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = (1 << len(nums) + 2) - 1
        for x in nums:
            if n & (1 << x):
                n ^= (1 << x)
            else:
                return x 
