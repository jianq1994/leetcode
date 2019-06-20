from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = deque()
        stack.append(root)
        ans = []
        while(stack):
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                for node in cur.children[::-1]:
                    stack.append(node)
        return ans
                    
            
        
        