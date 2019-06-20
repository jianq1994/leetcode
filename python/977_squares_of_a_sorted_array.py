class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        C = []
        D = []
        for a in A:
            if a <= 0:
                B.append(a*a)
            else:
                C.append(a*a)
        B = B[::-1]
        ib = 0
        ic = 0
        while(ib<len(B) and ic<len(C)):
            if B[ib] <= C[ic]:
                D.append(B[ib])
                ib += 1
            else:
                D.append(C[ic])
                ic += 1
        if ib == len(B):
            D.extend(C[ic:])
        else:
            D.extend(B[ib:])
        return D
        