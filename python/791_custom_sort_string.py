class Solution:
    def customSortString(self, S: str, T: str) -> str:
        
        def order(c):
            if c in S:
                return S.index(c)
            else:
                return 27
        tmp = list(T)
        tmp.sort(key=order)
        R="".join(tmp)
        return R