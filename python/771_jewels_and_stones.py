class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic = {}
        tot = 0
        for j in J:
            dic[j] = 0
        for s in S:
            if s in dic:
                dic[s] += 1
        for j in J:
            tot += dic[j]
        return tot