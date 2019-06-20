class Solution:
    
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        L = len(days)
        memo = {}
        for i in range(L+1):
            memo[(i,i)] = 0
        
        def recur(i,j,days,costs):
            if (i,j) in memo:
                return memo[(i,j)]
            opt1 = costs[0] + recur(i+1,j,days, costs)
            i1 = i
            while( i1<j and days[i1]<=days[i]+6):
                i1 += 1
            opt2 = costs[1] + recur(i1,j,days, costs)
            i2 = i
            while( i2<j and days[i2]<=days[i]+29):
                i2 += 1
            opt3 = costs[2] + recur(i2,j,days, costs)
            memo[(i,j)] = min([opt1,opt2,opt3])
            return memo[(i,j)]
        

        
        return recur(0,L,days,costs)
            