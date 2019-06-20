# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            root = TreeNode(val)
            return root
        if val > root.val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right,val)
            return root
        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left,val)
            return root
            
        