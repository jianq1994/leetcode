#81,13
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        traversed = []
        cur = [root]
        nextcur = []
        while(cur):
            for ele in cur:
                traversed.append(ele.val)
                if ele.left:
                    nextcur.append(ele.left)
                if ele.right:
                    nextcur.append(ele.right)
            cur = nextcur
            nextcur = []
            result.append(traversed)
            traversed = []
        return result