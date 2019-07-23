#22~66,5

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def isSym(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return (root1.val == root2.val) and isSym(root1.left, root2.right) and isSym(root1.right, root2.left)
        
        return isSym(root.left,root.right)