class Solution:
    memo = [0]
    def countBits(self, num: int) -> List[int]:
        L = len(Solution.memo)
        if num < L:
            return Solution.memo[:num+1]
        while(num >= L):
            ext = [1+a for a in Solution.memo]
            Solution.memo.extend(ext)
            L = len(Solution.memo)
        return Solution.memo[:num+1]
            