class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [format(i, 'b').count('1') for i in range(n+1)]
        return res
