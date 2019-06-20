from copy import deepcopy
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        
        H = len(A)
        L = len(A[0])
        down = deepcopy(A[H-1])
        up = []
        
        def minFalling(down,j):
            mini = float('inf')
            for s in (j-1,j,j+1):
                if -1<s<L:
                    mini = min(mini,down[s])
            return mini
            
        
        for h in range(H-2,-1,-1):
            for l in range(L):
                up.append(minFalling(down,l)+A[h][l])
            down = up
            up = []
        return min(down)
        