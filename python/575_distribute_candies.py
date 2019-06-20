from collections import Counter
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        L = len(candies)
        C = Counter(candies)
        if len(C) < L//2:
            return len(C)
        else:
            return L//2