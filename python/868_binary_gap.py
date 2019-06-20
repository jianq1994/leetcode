class Solution:
    def binaryGap(self, N: int) -> int:
        ans = 0
        r,l = -1,-1
        place = 0
        while(N):
            digit = N%2
            N = N//2
            if digit:
                if r == -1:
                    r=l=place
                else:
                    l=r
                    r=place
                    ans = max(ans,r-l)
            place += 1
        return ans