class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr,i):
			# base condition
            if i>=len(nums):
                res.append(curr.copy())
                return
				
			# include the value	
            curr.append(nums[i])
            dfs(curr,i+1)
            
			#don't include the value
            curr.pop()
            dfs(curr,i+1)
			
        dfs([],0)
        
        return res
