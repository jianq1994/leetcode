class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        H = len(A)
        L = len(A[0])
        for a in A:
            if a[0] == 0:
                for i in range(L):
                    a[i] = 1-a[i]
        ans = H * 2**(L-1)
        for i in range(1,L):
            vi = sum([A[h][i] for h in range(H)])
            if vi <= H/2:
                ans += (H-vi)*2**(L-i-1)
            else:
                ans += vi*2**(L-i-1)
        return ans
                
                    
                
                    