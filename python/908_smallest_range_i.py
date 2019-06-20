class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        mini,maxi = min(A),max(A)
        if maxi - mini > 2*K:
            return maxi -mini-2*K
        else:
            return 0