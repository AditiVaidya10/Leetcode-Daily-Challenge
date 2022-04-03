class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = len(nums)-1
        
        while index > 0:
            if nums[index] > nums[index-1]:
                break
            index -= 1
            
        if index == 0:
            nums.reverse()
            return
        else:
            next = index
            while next < len(nums) and nums[index-1] < nums[next]:
                next += 1
            nums[index-1], nums[next-1] = nums[next-1], nums[index-1]
            nums[index:] = nums[index:][::-1]
