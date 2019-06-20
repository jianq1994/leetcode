# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        val = root.val
        
        def unival(root):
            if not root:
                return True
            if root.val != val:
                return False
            else:
                return unival(root.left) and unival(root.right)
        
        return unival(root)