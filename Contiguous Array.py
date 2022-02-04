class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        a, b = 0,0
        c = {0:-1}
        for i in range(len(nums)):
            if nums[i] == 0:
                b -= 1
            else:
                b += 1
            if b in c:
                a = max(a, i-c[b])
            else:
                c[b] = i
        return a
