# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    memo = {0:[],1:[TreeNode(0)]}
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N not in Solution.memo:
            ans = []
            for x in range(1,N-1):
                leftChoice = self.allPossibleFBT(x)
                rightChoice = self.allPossibleFBT(N-1-x)
                for left in leftChoice:
                    for right in rightChoice:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        ans.append(root)
            Solution.memo[N] = ans
        return Solution.memo[N]