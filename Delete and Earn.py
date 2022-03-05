class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        money = Counter(nums)
        for num in money:
            money[num] = money[num] * num
        dp = [0] * (len(money.keys()) + 1)
        
        for idx, num in enumerate(sorted(money.keys())):
            if num - 1 in money:
                dp[idx + 1] = max(dp[idx], dp[idx - 1] + money[num])
            else:
                dp[idx + 1] = dp[idx] + money[num]
            
        return dp[-1]
