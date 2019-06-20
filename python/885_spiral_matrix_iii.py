from copy import deepcopy
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        
        def direction():
            while(1):
                for s,t in [[0,1],[1,0],[0,-1],[-1,0]]:
                    yield s,t
        
        ans = [[r0,c0]]
        step = 1
        turns = 4*max(R-r0,r0,C-c0,c0)
        cur = [r0,c0]
        d = direction()
        for i in range(turns):
            s,t = d.__next__()
            for i in range(step):
                cur[0] += s
                cur[1] += t
                if -1<cur[0]<R and -1<cur[1]<C:
                    ans.append(deepcopy(cur))
            s,t = d.__next__()
            for i in range(step):
                cur[0] += s
                cur[1] += t
                if -1<cur[0]<R and -1<cur[1]<C:
                    ans.append(deepcopy(cur))
            step += 1
        return ans
        
               
            
        