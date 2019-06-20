class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        H = len(grid)
        L = len(grid[0])
        maxi = 0
        
        def neigh(i,j):
            for s,t in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if -1<s<H and -1<t<L and grid[s][t] == 1:
                    yield s,t
        
        def dfs(i,j):
            grid[i][j] = 2
            aera = 1
            for s,t in neigh(i,j):
                aera += dfs(s,t)
            return aera
        
        for i in range(H):
            for j in range(L):
                if grid[i][j] == 1:
                    maxi = max(maxi, dfs(i,j))
        return maxi
                