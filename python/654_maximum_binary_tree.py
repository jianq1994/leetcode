# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maxval = max(nums)
        root = TreeNode(maxval)
        index = nums.index(maxval)
        leftRoot = self.constructMaximumBinaryTree(nums[:index])
        rightRoot = self.constructMaximumBinaryTree(nums[index+1:])
        root.left = leftRoot
        root.right = rightRoot
        return root 
        