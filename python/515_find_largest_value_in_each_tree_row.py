# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = [root.val]
        lans = self.largestValues(root.left)
        rans = self.largestValues(root.right)
        L = len(lans)
        R = len(rans)
        M = min(L,R)
        for i in range(M):
            ans.append(max(lans[i],rans[i]))
        ans.extend(lans[M:])
        ans.extend(rans[M:])
        return ans