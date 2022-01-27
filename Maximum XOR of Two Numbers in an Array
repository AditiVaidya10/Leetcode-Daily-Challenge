class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        t, task = 0, 0
        for i in range(32)[::-1]:
            task |= 1 << i
            prefixes = {n & task for n in nums}
            tmp = t | (1 << i)
            if any(prefix ^ tmp in prefixes for prefix in prefixes):
                t = tmp
        return t
