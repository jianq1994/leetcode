class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x
        while(l<r):
            m = (1+l+r)//2
            if x/m >= m: l = m
            else: r = m-1
        return l