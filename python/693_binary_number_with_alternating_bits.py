class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if not n:
            return True
        strrep = str(bin(n))[2:]
        val = int(strrep[0])
        for num,i in enumerate(strrep):
            if int(i) == (1+(-1)**num)//2:
                pass
            else:
                return False
        return True