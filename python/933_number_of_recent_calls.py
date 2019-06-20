class RecentCounter:

    def __init__(self):
        self.memo = []

    def ping(self, t: int) -> int:
        
        def search(L,val):
            if not L:
                return 0
            l = 0
            r = len(L)-1
            R = len(L)-1
            while(l<r):
                m = (l+r)//2
                if L[m] == val:
                    return R-m+1
                elif L[m] < val:
                    if L[m+1] >= val:
                        return R-m
                    else:
                        l = m+1
                else:
                    if m-1 < l:
                        return R-m+1
                    elif L[m-1] < val:
                        return R-m+1
                    else:
                        r=m-1
            return R-l+1
        
        if not t:
            return None
        else:
            self.memo.append(t)
            return search(self.memo,t-3000)
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)