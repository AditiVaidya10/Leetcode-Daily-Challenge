class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for start in range(n - 1):  
            for end in range(start + 1, n):  
                subarray_sum = sum(nums[start:end + 1])  
                if subarray_sum == 0 and k == 0:  
                    return True
                if k != 0 and subarray_sum % k == 0: 
                    return True
        return False  
