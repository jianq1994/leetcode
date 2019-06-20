class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # if not s:
        #     return s
        # idxl = 0
        # idxr = len(s)-1
        # while(idxr>idxl):
        #     tmp = s[idxl]
        #     s[idxl] = s[idxr]
        #     s[idxr] = tmp
        s[:] = s[::-1]