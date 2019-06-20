class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        H = len(grid)
        L = len(grid[0])
        
        
        def neigh(i,j):
            nei = []
            for s,t in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if -1<s<H and -1<t<L and (grid[s][t] == 1 or grid[s][t] == 2):
                    nei.append((s,t))
            return nei
        
        def dfs(i,j):
            grid[i][j] = 2
            nei = neigh(i,j)
            ans = 4 - len(nei)
            for s,t in neigh(i,j):
                if grid[s][t] == 1:
                    ans += dfs(s,t)
            return ans
        
        for i in range(H):
            for j in range(L):
                if grid[i][j] == 1:
                    return dfs(i,j)