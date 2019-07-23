#30,5, recursive is slow

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def withRangeValid(root):
            if not root:
                return None, None, True
            if not root.left and not root.right:
                return root.val, root.val, True
            if not root.left:
                rmin, rmax, rv = withRangeValid(root.right)
                return root.val, rmax, (rv and root.val<rmin)
            if not root.right:
                lmin, lmax, lv = withRangeValid(root.left)
                return lmin, root.val, (lv and root.val>lmax)             
            lmin, lmax, lv = withRangeValid(root.left)
            rmin, rmax, rv = withRangeValid(root.right)
            return lmin, rmax, (lv and rv and lmax<root.val<rmin)
        
        return withRangeValid(root)[2]


#30,18, copied from others
class Solution:
    def check_order(self, node, lower=-float('inf'), upper=float('inf')):
        if node is None:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        return self.check_order(node.left, lower, min(node.val, upper)) and self.check_order(node.right, max(lower, node.val), upper)


    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_order(root)

#67~86,21~23


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        checkright = []
        cur = root
        receive = -float('inf')
        while(1):
            while(cur.left):
                checkright.append(cur)
                cur = cur.left
            if receive >= cur.val:
                return False
            receive = cur.val
            while(not cur.right):
                if not checkright:
                    return True
                cur = checkright.pop()
                if receive >= cur.val:
                    return False
                receive = cur.val    
            cur = cur.right
            



