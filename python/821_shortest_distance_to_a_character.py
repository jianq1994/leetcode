class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        L = len(S)
        ans = [float('inf')] * L
        front = None
        for l,s in enumerate(S):
            if s == C:
                front = l
                ans[l] = 0
            elif front is not None:
                ans[l] = l-front
        front = None
        for l in range(-1,-L-1,-1):
            if S[l] == C:
                front = l
            elif front is not None:
                ans[l] = min(ans[l], abs(l-front))
        return ans
            
        
                