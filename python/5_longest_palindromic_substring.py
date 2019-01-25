class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        maxlen = 0
        maxstr = ''
        table = [[False for j in range(len(s)+1)] for i in range(len(s))]
        for i in range(len(s)):
            table[i][i+1] = True
        for l in range(1,len(s)+1):
            for i in range(len(s)-l+1):
                j = i+l
                if s[i] == s[j-1] and (i+2>=j or table[i+1][j-1]):
                    table[i][j] = True
                    if l>maxlen:
                        maxlen = l
                        maxstr = s[i:j]
        return maxstr