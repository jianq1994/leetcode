class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {}
        for num, s in enumerate(S):
            if s in dic:
                dic[s][1] = num
            else:
                dic[s] = [num,num]
        
        def partWithDic(S, displace):
            if displace >= len(S):
                return []
            ans =[]
            a = S[displace]
            r1 = displace
            r2 = dic[a][1]
            r3 = dic[a][1]
            while(1):
                r3 = r2
                for i in range(r1,r2):
                    if dic[S[i]][1] > r2:
                        r2 = dic[S[i]][1]
                r1 = r3
                if r1 == r2:
                    ans = [r2-displace+1]
                    ans.extend(partWithDic(S,r1+1))
                    return ans
        return partWithDic(S,0)
                    