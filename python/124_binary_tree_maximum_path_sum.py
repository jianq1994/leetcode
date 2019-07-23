#98,5

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def withlong(root):
            if not root.left and not root.right:
                return root.val, root.val
            if not root.left:
                rm,rl = withlong(root.right)
                return max([rm,rl+root.val, root.val]), max([rl+root.val,root.val])
            if not root.right:
                lm,ll = withlong(root.left)
                return max([lm,ll+root.val, root.val]), max([ll+root.val,root.val])
            lm,ll = withlong(root.left)
            rm,rl = withlong(root.right)
            return max([lm,rm,ll+rl+root.val,ll+root.val,rl+root.val,root.val]), max([ll,rl,0])+root.val
        
        return withlong(root)[0]