class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(candidates, target ,path):
            if target == 0:
                result.append(path)
            elif not candidates or target < candidates[0]:
                return
            else:
                for i, c in enumerate(candidates):
                    dfs(candidates[i:], target -c, path + [c])
        dfs(candidates, target, [])
        return result
