class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        nxt = [float('inf')]*102
        ans = []
        for i in range(len(T)-1,-1,-1):
            lo = min(nxt[T[i]+1:])
            if lo == float('inf'):
                ans.append(0)
            else:
                ans.append(lo-i)
            nxt[T[i]] = i
        return ans[::-1]
            