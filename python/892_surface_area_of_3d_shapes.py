class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        H = len(grid)
        L = len(grid[0])
        ans = 0
        
        
        def neigh(i,j):
            for s,t in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if -1<s<H and -1<t<L:
                    yield s,t
        def relu(a,b):
            if a>=b:
                return a-b
            else:
                return 0
        
        
        for i in range(H):
            for j in range(L):
                if grid[i][j] != 0:
                    ans += 2
                if i == 0:
                    ans += grid[i][j]
                if i == H-1:
                    ans += grid[i][j]
                if j == 0:
                    ans += grid[i][j]
                if j == L-1:
                    ans += grid[i][j]
                for s,t in neigh(i,j):
                    ans += relu(grid[i][j],grid[s][t])
        
        return ans
                
                    