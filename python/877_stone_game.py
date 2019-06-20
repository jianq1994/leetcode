class Solution:
    def stoneGame(self, piles):
        L = len(piles)
        self.memo = {}
        
        def dp(i,j,turn):
            if (i,j,turn) in self.memo:                
                return self.memo[(i,j,turn)]
            if i==j:
                if turn:
                    self.memo[(i,j,turn)] = piles[i]
                else:
                    self.memo[(i,j,turn)] = -piles[i]
            elif turn:
                self.memo[(i,j,turn)] = max(dp(i+1,j,0)+piles[i], dp(i,j-1,0)+piles[j])
            else:
                self.memo[(i,j,turn)] = min(dp(i+1,j,1)-piles[i], dp(i,j-1,1)-piles[j])
            return self.memo[(i,j,turn)]
        
        if dp(0,L-1,1) > 0:
            return True
        return False