class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def sumRootToLeaf(root, res):
            if root == None: return 0
            res = (2*res) + root.val
            if root.left == None and root.right == None: return res
            return sumRootToLeaf(root.left, res) + sumRootToLeaf(root.right, res)
        return sumRootToLeaf(root, 0)
