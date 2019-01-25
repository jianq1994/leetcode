from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        maxlen = 1
        rec = deque()
        rec.append(s[0])
        for c in s[1:]:
            if c in rec:
                maxlen = max(maxlen, len(rec))
                watch = rec.popleft()
                while(watch!=c):
                    watch = rec.popleft()
                rec.append(c)
            else:
                rec.append(c)
        maxlen = max(maxlen, len(rec))
        return maxlen