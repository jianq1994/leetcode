class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ans = ''
        SS = ''
        for s in S:
            if s.isalpha():
                ans += s
        idx = -1
        for s in S:
            if s.isalpha():
                SS += ans[idx]
                idx -= 1
            else:
                SS += s
        return SS
        