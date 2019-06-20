class Solution:
    def pancakeSort(self, A):
        ans = []
        L = len(A)
        for i in range(L,0,-1):
            idx = A.index(i)
            if idx+1 == i:
                pass
            else:
                ans.append(idx+1)
                A[:idx+1] = A[:idx+1][::-1]
                ans.append(i)
                A[:i] = A[:i][::-1]
        return ans