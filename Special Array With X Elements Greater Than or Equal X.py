import bisect

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums=sorted(nums)
        n=len(nums)
        for i in range(n,0,-1):
        // It will find the ind at which the element is to be inserted
            k=bisect.bisect_left(nums,i)
            if(n-k==i):
                return i
        return -1
