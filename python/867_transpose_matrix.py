class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return []
        H,L = len(A),len(A[0])
        B = []
        for l in range(L):
            B.append([A[h][l] for h in range(H)])
        return B