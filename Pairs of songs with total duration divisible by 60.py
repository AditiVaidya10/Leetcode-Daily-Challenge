class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dp = [0]*60
        res = 0
        for t in time:
            rem = t % 60
            target = (60 - rem) % 60
            res += dp[target]
            dp[rem] += 1
        return res
