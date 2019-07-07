class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        l,r = 0,len(matrix)-1
        while(l<r):
            m = (l+r+1)//2
            if matrix[m][0] == target: 
                return True
            elif matrix[m][0] < target:
                l = m
            else:
                r = m-1
        # if matrix[l][0] == target: 
        #     return True
        m,l,r = l,0,len(matrix[0])-1
        while(l<r):
            mm = (l+r+1)//2
            if matrix[m][mm] == target: 
                return True
            elif matrix[m][mm] < target:
                l = mm
            else:
                r = mm-1
        return matrix[m][l] == target