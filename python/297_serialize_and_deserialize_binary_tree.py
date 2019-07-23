#77,19
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null'
        result = ''
        front = [root]
        nextfront = []
        notallnull = 1
        while(front and notallnull):
            notallnull = 0
            for cur in front:
                if not cur:
                    result += ',null'
                else:
                    result += ',' + str(cur.val)
                    nextfront.append(cur.left)
                    nextfront.append(cur.right)
                    if cur.left or cur.right:
                        notallnull = 1
            front = nextfront
            nextfront = []
        return result[1:]
        

            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dummy = TreeNode(0)
        data =  'null,'+data
        data = data.split(',')
        position = [dummy]
        nextposition = []
        i = 0
        while(data[i:]):
            for node in position:
                if data[i] != 'null':
                    node.left = TreeNode(int(data[i]))
                    nextposition.append(node.left)
                if data[i+1] != 'null':
                    node.right = TreeNode(int(data[i+1]))
                    nextposition.append(node.right)
                i += 2
            position = nextposition
            nextposition = []
        return dummy.right