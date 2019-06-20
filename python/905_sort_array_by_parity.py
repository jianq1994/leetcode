class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        C = []
        for a in A:
            if a%2 == 0:
                C.append(a)
            else:
                B.append(a)
        C.extend(B)
        return C