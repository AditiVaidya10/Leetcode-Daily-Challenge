class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, last = 0, -1
        for i, seat in enumerate(seats):
            if seat:
                res = max(res, (i - last) // 2 if last >= 0 else i)
                last = i
        return max(res, len(seats) - 1 - last if not seats[-1] else 0)
