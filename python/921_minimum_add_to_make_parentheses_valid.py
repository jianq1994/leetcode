class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        L,R,uselessR = 0,0,0
        for s in S:
            if s == '(':
                L += 1
            elif s == ')':
                if L > 0:
                    L -= 1
                else:
                    uselessR += 1
        return L+uselessR    