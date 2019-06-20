from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result =[]
        st =[root]
        while st:
            node = st.pop()
            if node:
                result.append(node.val)    
                for item in node.children:
                    st.append(item)
        return result[::-1]
