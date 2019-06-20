class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        H, L = len(grid), len(grid[0])
        
        def neigh(h,l):
            for x,y in [(h-1,l),(h+1,l),(h,l+1),(h,l-1)]:
                if -1 < x and x < H and -1 < y and y < L and grid[x][y]%2==0:
                    yield x,y
        
        self.ans = 0
        Trest = 0
        for i in range(H):
            for j in range(L):
                if grid[i][j] == 0:
                    Trest += 1
                elif grid[i][j] == 1:
                    si,sj = i,j
                elif grid[i][j] == 2:
                    Trest += 1
                    oi,oj = i,j
        
        def dps(i,j,rest):
            if rest == 0 and i == oi and j == oj:
                self.ans += 1
                return 
            elif i == oi and j == oj:
                return 
            rest -= 1
            grid[i][j] = -1
            for x,y in neigh(i,j):
                dps(x,y,rest)
            grid[i][j] = 0
            return 
        dps(si,sj,Trest)
        return self.ans
                    
        
        