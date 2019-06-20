from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        sl = list(s)
        sl.sort(key =lambda x: (c[x],ord(x)),reverse=True)
        return ''.join(sl)