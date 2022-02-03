class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums12, res = defaultdict(int), 0
        for i in nums1:
            for j in nums2:
                nums12[i+j] += 1
        for k in nums3:
            for l in nums4:
                res += nums12[-(k+l)]
        return res
