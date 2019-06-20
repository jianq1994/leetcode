class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        if not S:
            return [0,0]
        line = 1
        last = 0
        for s in S:
            if last + widths[ord(s)-ord('a')] > 100:
                line += 1
                last = widths[ord(s)-ord('a')]
            else:
                last = last + widths[ord(s)-ord('a')]
        return [line,last]