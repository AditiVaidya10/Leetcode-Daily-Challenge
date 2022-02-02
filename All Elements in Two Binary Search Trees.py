class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        heap = []
        heapq.heapify(heap)
        def dfs(node):
            if node:
                heapq.heappush(heap, node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root1)
        dfs(root2)
        return heapq.nsmallest(len(heap), heap)
