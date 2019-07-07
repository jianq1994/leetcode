class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        l,r,L = 0, len(citations)-1,len(citations)
        while(l<r):
            m = (l+r)//2
            if citations[m] >= L-m:
                r = m
            else:
                l = m+1
        if citations[l] >= L-l:
            return L-l
        else:
            return L-l-1
        
        
        
        
        # for i in range(len(citations)):
        #     if citations[-i-1] >= i+1:
        #         i = i+1
        #     else:
        #         break
        # return i
    
