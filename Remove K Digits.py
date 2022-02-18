class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num or k >= len(num):
            return "0"
        ans = []
        t = k
        for i in num:
            while ans and ans[-1] > i and t > 0:
                ans.pop()
                t -= 1
            ans.append(i)
        for i in range(t):
            ans.pop()
        res = "".join(ans).lstrip('0')
        return '0' if not res else res
