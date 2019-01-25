class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = []
        result = ''
        for j in range(numRows):
            rows.append('')
        for i,char in enumerate(s):
            idx = i % (2*numRows-2)
            if idx < numRows:
                rows[idx] += char
            else:
                rows[numRows-2-idx] += char
        for j in range(numRows):
            result += rows[j]
        return result