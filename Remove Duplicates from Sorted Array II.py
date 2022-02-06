class Solution:
    def removeDuplicates(self, nums) -> int:
        prev = nums[0]
        count = 1
        idx = 1
        while idx < len(nums):
            if nums[idx] == prev:
                if count < 2:
                    count += 1
                    idx += 1
                else:
                    nums.pop(idx)
            else:
                prev = nums[idx]
                count = 1
                idx += 1
        return idx      
