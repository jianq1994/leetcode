class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        if len(points)<3:
            return 0
        
        def aera(a,b,c):
            return abs(a[0]*b[1]-b[0]*a[1] + b[0]*c[1]-c[0]*b[1] + c[0]*a[1] - a[0]*c[1])/2
        
        
        L =len(points)
        maxi = 0
        for i in range(L):
            for j in range(L-1):
                for k in range(L-2):
                    maxi = max(maxi, aera(points[i],points[j],points[k]))
        return maxi