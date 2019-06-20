# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def leafTra(root):
            if not root:
                return []
            ans = []
            if not root.left and not root.right:
                ans.append(root.val)
                return ans
            ans.extend(leafTra(root.left))
            ans.extend(leafTra(root.right)) 
            return ans
        
        rt1 = leafTra(root1)
        rt2 = leafTra(root2)
        if rt1 == rt2:
            return True
        return False