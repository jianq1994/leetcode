class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        length = len(grid)
        Tskyline = [0] * length
        Lskyline = [0] * length
        for i in range(length):
            for j in range(length):
                Lskyline[i] = max(Lskyline[i], grid[i][j])
                Tskyline[j] = max(Tskyline[j], grid[i][j])
        tot = 0
        for i in range(length):
            for j in range(length):
                tot += (min(Lskyline[i], Tskyline[j]) - grid[i][j])
        return tot
            