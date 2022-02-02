class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1] 
        mem = collections.defaultdict(int)
        def search(nums):
            if tuple(nums) in mem: 
                return mem[tuple(nums)]
            ans = [0] * len(nums)
            for i in range(1, len(nums) - 1):
                ans[i] = search(nums[:i + 1]) + search(nums[i:]) + nums[0] * nums[i] * nums[-1]
            mem[tuple(nums)] = max(ans)
            return mem[tuple(nums)]

        return search(nums)
