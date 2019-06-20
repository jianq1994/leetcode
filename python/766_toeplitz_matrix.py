class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix: return True
        H = len(matrix)
        L = len(matrix[0])
        for l in range(L):
            cur = [0,l]
            val = matrix[0][l]
            flag = 0
            while(cur[0]<H and cur[1]<L):
                if matrix[cur[0]][cur[1]] == val:
                    cur[0] += 1
                    cur[1] += 1
                else:
                    flag = 1
                    break
            if flag:
                return False
        
        for h in range(1,H):
            cur = [h,0]
            val = matrix[h][0]
            flag = 0
            while(cur[0]<H and cur[1]<L):
                if matrix[cur[0]][cur[1]] == val:
                    cur[0] += 1
                    cur[1] += 1
                else:
                    flag = 1
                    break
            if flag:
                return False
        return True
            