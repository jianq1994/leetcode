#82,5

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        
        def Findwithnotice(root,p,q):
            if not root:
                return False, False, None
            lp, lq, lnode = Findwithnotice(root.left,p,q)
            if lnode:
                return None, None, lnode
            rp, rq, rnode = Findwithnotice(root.right,p,q)
            if rnode:
                return None, None, rnode
            if (lp or rp or root == p) and (lq or rq or root == q):
                return True, True, root
            return (lp or rp or root == p), (lq or rq or root == q), None
        
        return Findwithnotice(root,p,q)[2]