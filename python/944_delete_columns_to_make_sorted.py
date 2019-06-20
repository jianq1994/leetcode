class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if not A:
            return 0
        ans = 0
        for c in range(len(A[0])):
            flag = 0
            for i in range(len(A)-1):
                if ord(A[i][c]) > ord(A[i+1][c]):
                    flag = 1
                    break
            if flag:
                ans += 1
        return ans