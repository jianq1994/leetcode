from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 14,5
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = deque([root])
        cur = root
        ans = []
        while(stack):
            if cur.left:
                stack.append(cur.left)
                cur = cur.left
            else:
                # ans.append(cur.val)
                cur = stack.pop()
                while(not cur.right and stack):
                    ans.append(cur.val)
                    cur = stack.pop()
                ans.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                    cur = cur.right
                else:
                    return ans

#66~88,5

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res                 
        