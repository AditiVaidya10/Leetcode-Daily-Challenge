class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == val:
            return root
        def helper(root, val):
            if root == None:
                return root
            if val > root.val:
                return helper(root.right, val)
            if val < root.val:
                return helper(root.left, val)
            if val == root.val:
                return root
        return helper(root, val)
