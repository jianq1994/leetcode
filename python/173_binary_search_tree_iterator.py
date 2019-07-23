#91,5

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.prelist = []
        self.cur = root
        if root:
            while(self.cur.left):
                self.prelist.append(self.cur)
                self.cur = self.cur.left
        
            
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        ans = self.cur.val
        if self.cur.right:
            self.cur = self.cur.right
            while(self.cur.left):
                self.prelist.append(self.cur)
                self.cur = self.cur.left
        else:
            if self.prelist:
                self.cur = self.prelist.pop()
            else:
                self.cur = None
        return ans
            

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.prelist or self.cur:
            return True
        else:
            return False