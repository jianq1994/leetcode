# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        
        def findWithHeight(root):
            if not root.left and not root.right:
                return (root.val,0)
            elif not root.left:
                x,y = findWithHeight(root.right)
                return (x, y+1)
            elif not root.right:
                x,y = findWithHeight(root.left)
                return (x, y+1)
            else:
                x1,y1 = findWithHeight(root.left)
                x2,y2 = findWithHeight(root.right)
                if y1 >= y2:
                    return (x1,y1+1)
                else:
                    return (x2,y2+1)
        
        x,_ = findWithHeight(root)
        return x