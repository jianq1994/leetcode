#85,5

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def withlongandlarge(root):
            if not root:
                return 0,0
            lm,ll = withlongandlarge(root.left)
            rm,rl = withlongandlarge(root.right)
            return max([lm,rm,ll+rl+1]),max([ll,rl])+1
        
        return withlongandlarge(root)[0]-1