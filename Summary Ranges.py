class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
        op = []
        temp = ""
        i, j = 0, 0
        while i < len(nums):
            while j < len(nums)-1 and nums[j] == nums[j+1] - 1:
                j += 1
            if i == j:
                op.append(str(nums[i]))
            else:
                op.append(str(nums[i]) + "->" + str(nums[j]))
            j += 1
            i = j
        return op
