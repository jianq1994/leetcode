# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        ans = []
        pre = []
        postval = []
        post = [root]
        while(1):
            pre = post
            post = []
            preval = []
            while(pre):
                cur = pre.pop()                
                if cur:
                    preval.append(cur.val)
                    post.append(cur.left)
                    post.append(cur.right)
            if not preval:
                break
            else:
                ans.append(sum(preval)/len(preval))
        return ans
                    