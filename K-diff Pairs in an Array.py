class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        s = set()
        result = set()
        for i in range(n):
            if nums[i] in s:
                result.add(tuple([nums[i]-k, nums[i]]))
            s.add(nums[i]+k)
        return len(result)
