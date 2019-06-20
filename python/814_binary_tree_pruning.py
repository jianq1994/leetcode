# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return None
        if root.val == 0 and root.left == None and root.right == None:
            return None
        if root.val == 0:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if root.left == None and root.right == None:
                return None
        else:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
        return root
            
        