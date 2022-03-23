class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        output = 0

        while startValue < target:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1

            output += 1

        return output + (startValue - target)
