class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0 
        for i,char in enumerate(str+'#'):
            if char == ' ':
                pass
            elif char not in '+-0123456789':
                return 0
            else:
                break
        if char in '+-':
            i += 1 
        if i == len(str) or str[i] not in '0123456789':
            return 0
        sign = 1
        num = 0
        if char == '-':
            sign = 0
        for j,char in enumerate(str[i:]+'#'):
            if char in '0123456789':
                pass
            else:
                break
        num = int(str[i:i+j])
        if not sign:
            if num >= 2**31:
                return -2**31
            num = -num
        else:
            if num >= 2**31-1:
                return 2**31-1
        return num