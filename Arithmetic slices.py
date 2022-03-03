class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        subarrays_before, count = 0, 0
        diff = -inf
        for i in range(1, len(nums)):
            new_diff = nums[i] - nums[i-1]
            if new_diff == diff:
                count += 1 + subarrays_before
                subarrays_before += 1
            else:
                subarrays_before = 0
            diff = new_diff
        return count
