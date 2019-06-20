class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        eidx = 0
        oidx = 1
        ans = [0]*len(A)
        for a in A:
            if a%2 == 0:
                ans[eidx] = a
                eidx += 2
            else:
                ans[oidx] = a
                oidx += 2
        return ans