class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car, increase = 0, [0] * 1001
        for [a, f, t] in trips:
            increase[f] += a
            increase[t] -= a
        for i in range(0, 1001):
            car += increase[i]
            if car > capacity:
                return False
        return True
