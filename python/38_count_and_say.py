class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        cac = '1'
        ncac = ''
        count = 0
        number = 0
        for i in range(n-1):
            number = int(cac[0])
            count = 0
            for c in cac:
                if int(c) == number:
                    count += 1
                else:
                    ncac += str(count)
                    ncac += str(number)
                    number = int(c)
                    count = 1
            ncac += str(count)
            ncac += c
            cac = ncac
            ncac = ""
        return cac
                