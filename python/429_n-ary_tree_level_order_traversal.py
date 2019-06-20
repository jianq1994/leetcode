"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans =[]
        pre = []
        preval = []
        pos = [root]
        while(pos):
            pre = pos
            preval = []
            pos = []
            for cur in pre:
                pos.extend(cur.children)
                preval.append(cur.val)
            ans.append(preval)
        return ans
                