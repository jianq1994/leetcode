# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        if not root.left:
            root.right = self.increasingBST(root.right)
            return root
        pre = root
        cur = root.left
        while(cur.left):
            cur = cur.left
            pre = pre.left
        pre.left = cur.right
        cur.right = self.increasingBST(root)
        return cur
        